from abc import ABC, abstractmethod
from typing import Any, override
import pandas as pd, requests, logging
import sqlite3

from datetime import datetime, timedelta, timezone
from json import dumps as jdumps

class Fetcher(ABC):
    def __init__(self, api_endpoint:str, cache_db_path:str, expiration_s:int=30):
        super().__init__()

        self.cache_db = cache_db_path
        self.endpoint = api_endpoint
        self.expiration = expiration_s
        self.logger =logging.getLogger(self.__class__.__name__)

        with sqlite3.connect(self.cache_db) as conn:
            self.init_db(conn)

    @abstractmethod
    def get(self, tick, params) -> pd.DataFrame:
        pass

    def init_db(self, conn:sqlite3.Connection):
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS t_Cache (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Price REAL NOT NULL,
                Timestamp DATETIME NOT NULL,
                Tick TEXT NOT NULL,
                Params TEXT NOT NULL,
                Expiration DATETIME NOT NULL
            )
        """)


        cursor.execute("CREATE INDEX IF NOT EXISTS idx_cache_tick ON t_Cache(Tick)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_cache_params ON t_Cache(Params)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_cache_expiration ON t_Cache(Expiration)")

        self.logger.info("Database connection initialized")

    def delete_expired(self, conn:sqlite3.Connection):
        cursor = conn.cursor()

        cursor.execute("DELETE FROM t_Cache WHERE Expiration < CURRENT_TIMESTAMP")
        self.logger.info("Expired records pruned")


class CryptoFetcher(Fetcher):
    def fetch_data(self, params) -> dict[str, Any]:
        self.logger.info("Fetching!")
        response = requests.get(self.endpoint, params)
        return response.json()
    
    def check_data(self, data:dict[str, Any]) -> bool:
        if "status" in data:
            self.logger.warning(data["status"])
            return False
        
        if "error" in data:
            self.logger.warning(data["error"])
            return False
        
        return True

    def format_data(self, data:dict[str, Any]) -> pd.DataFrame|None:
        if not self.check_data(data):
            return None
        
        df = pd.DataFrame()
        df["Timestamp"], df["Price"] = zip(*data["prices"])
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="ms")

        self.logger.info("Formatted!")
        return df
    
    def cache_data(self, conn:sqlite3.Connection, tick:str, params:dict, data:pd.DataFrame|None) -> bool:
        if data is None: return False

        data["Expiration"] = datetime.now(timezone.utc) + timedelta(seconds=self.expiration)

        data["Params"] = jdumps(params)
        data["Tick"] = tick

        data.to_sql("t_Cache", conn, index=False, if_exists="append")
        self.logger.info("Cached!")
        return True


    def get_cached(self, conn:sqlite3.Connection, tick:str, params:dict):
        df:pd.DataFrame = pd.read_sql("""
            SELECT Price, Timestamp FROM t_Cache
            WHERE Params = ? AND Tick = ? AND Expiration >= CURRENT_TIMESTAMP
        """, conn, params=(jdumps(params), tick), parse_dates={"Timestamp" : {"format":"ISO8601"}}) #! parse dates

        if df.empty:
            self.logger.info("Expired or empty!")
            return None
        
        self.logger.info("Cache hit!")
        return df


    @override
    def get(self, tick, params) -> pd.DataFrame|None:
        # Check if data with these params ar in db
        # If yes: Return those (*format)
        # If not:
        #   Fetch
        #   Format
        #   Save to db
        #   Return

        with sqlite3.connect(self.cache_db) as conn:
            self.delete_expired(conn)

            if (d := self.get_cached(conn, tick, params)) is not None:
                return d
            
            data = self.fetch_data(params)
            data = self.format_data(data)

            if self.cache_data(conn, tick, params, data):
                return data[["Price", "Timestamp"]]
            
            return None
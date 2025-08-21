from abc import ABC, abstractmethod
from typing import Any, override
import pandas as pd
import requests

import sqlite3
import logging

from json import dumps as jdumps
from datetime import datetime, timedelta, timezone


class Fetcher(ABC):
    def __init__(self, api_endpoint:str, cache_db_path:str, expiration_s:int=30):
        super().__init__()

        self.endpoint = api_endpoint
        self.cache_db = cache_db_path
        self.expiration = expiration_s
        self.logger = logging.getLogger("fetcher")

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

    def update_db(self, conn:sqlite3.Connection):
        self.init_db(conn)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM t_Cache WHERE Expiration < CURRENT_TIMESTAMP")



class CryptoFetcher(Fetcher):
    def fetch_data(self, params) -> dict[str, Any]:
        self.logger.info("Fetching!")
        response = requests.get(self.endpoint, params)

        return response.json()
    
    def format_data(self, data:dict[str, Any]):
        if "status" in data:
            self.logger.info(data["status"])
            return None
        
        if "error" in data:
            self.logger.info(data["error"])
            return None
        
        df = pd.DataFrame()
        df["Timestamp"], df["Price"] = list(zip(*data["prices"]))
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="ms")

        self.logger.info("Formatted!")
        return df

    def cache_data(self, conn:sqlite3.Connection, tick:str, params:dict, data:pd.DataFrame|None) -> bool:
        if data is None: return False

        data["Expiration"] = datetime.now(timezone.utc) + timedelta(seconds=self.expiration) #! utc!

        data["Params"] = jdumps(params)
        data["Tick"] = tick

        data.to_sql("t_Cache", conn, index=False, if_exists="append")
        self.logger.info("Cached!")
        return True

    def get_cached(self, conn:sqlite3.Connection, tick:str, params:dict):
        df:pd.DataFrame = pd.read_sql("""
            SELECT Price, Timestamp FROM t_Cache
            WHERE Params = ? AND Tick = ? AND Expiration >= CURRENT_TIMESTAMP
        """, conn, params=(jdumps(params), tick), parse_dates={"Timestamp" : {"format" : "ISO8601"}}) #! parse dates

        if df.empty:
            self.logger.info("Expired or empty!")
            return None
        
        self.logger.info("Cache hit!")
        return df

    @override
    def get(self, tick, params) -> pd.DataFrame:
        # Check if data with these params are in db
        # If yes: Return those
        # If not:
        #   Fetch
        #   Format
        #   Save to db
        #   Return

        with sqlite3.connect(self.cache_db) as conn:
            self.update_db(conn)

            if (d := self.get_cached(conn, tick, params)) is not None:
                return d
            
            data = self.fetch_data(params)
            data = self.format_data(data)
            if self.cache_data(conn, tick, params, data):
                return data[["Price", "Timestamp"]]
            
            return None

class ShareFetcher(Fetcher):
    @override
    def get(self, tick, params) -> pd.DataFrame:
        pass
from abc import ABC, abstractmethod
from typing import override
from datetime import datetime, timedelta, timezone
from json import dumps as jdumps
import pandas as pd
import requests
import logging
import sqlite3



class Fetcher(ABC):
    def __init__(self, api_endpoint:str, cache_db:str, expiration_s:int=180, log_level=logging.CRITICAL):
        super().__init__()

        self.expiration = expiration_s
        self.cache_db = cache_db
        self.endpoint = api_endpoint
        logging.basicConfig(level=log_level)

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
    def fetch_data(self, params:dict = None):
        response = requests.get(self.endpoint, params)
        logging.debug("Fetched raw!")
        return response.json()
    
    def format_data(self, data:dict):
        if "status" in data:
            logging.debug(data["status"])
            return None
        
        if "error" in data:
            logging.debug(data["error"])
            return None
        
        df = pd.DataFrame()
        df["Timestamp"], df["Price"] = list(zip(*data["prices"]))
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="ms", utc=True)

        return df

    def get_cached(self, conn:sqlite3.Connection, tick:str, params:dict):
        df:pd.DataFrame = pd.read_sql("""
                SELECT Price, Timestamp FROM t_Cache
                WHERE Params = ? AND Tick = ? AND Expiration >= CURRENT_TIMESTAMP
            """, conn, params=(jdumps(params), tick), parse_dates={"Timestamp": {"format": "ISO8601"}})
        
        if df.empty:
            logging.debug("Expired or empty")
            return None
        
        logging.debug("Cache hit!")
        return df
    
    def cache_data(self, conn:sqlite3.Connection, tick:str, data:pd.DataFrame | None, params:dict = None):
        if data is None: return

        data["Expiration"] = datetime.now(timezone.utc) + timedelta(seconds=self.expiration)

        data["Params"] = jdumps(params)
        data["Tick"] = tick

        data.to_sql("t_Cache", conn, if_exists="append", index=False)
        logging.debug("Cached!")


    @override
    def get(self, tick, params) -> pd.DataFrame:
        with sqlite3.connect(self.cache_db) as conn:
            self.update_db(conn)

            if (d := self.get_cached(conn, tick, params)) is not None:
                return d

            data = self.fetch_data(params)
            data = self.format_data(data)
            self.cache_data(conn, tick, data, params)

        if data is None:
            return None

        return data[["Price", "Timestamp"]]
    
class ShareFetcher(Fetcher):
    @override
    def get(self, tick, params) -> pd.DataFrame:
        pass


if __name__ == "__main__":
    tick = "ethereum"
    url = f"https://api.coingecko.com/api/v3/coins/{tick}/market_chart"
    params = {"vs_currency":"usd", "days":5}
    f = CryptoFetcher(url, "CryptoCheck_cache.db", log_level=logging.DEBUG)

    df = f.get(tick, params)
    print(df)
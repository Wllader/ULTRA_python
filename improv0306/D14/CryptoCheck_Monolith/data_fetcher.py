from abc import ABC, abstractmethod
from typing import override, Any
import pandas as pd
import requests

import sqlite3
from json import dumps as jdumps

from datetime import datetime, timedelta, timezone
import logging

class Fetcher(ABC):
    def __init__(self, api_endpoint:str, cache_db:str, expiration_s:int=30, log_level=logging.CRITICAL):
        super().__init__()

        self.endpoint = api_endpoint # Template-strings coming in Python 3.14
        self.cache_db = cache_db
        self.expiration = expiration_s
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
                Params TEXT NOT NULL ,
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
    def fetch_data(self, params):
        logging.info("Fetching!")

        response = requests.get(self.endpoint, params)
        return response.json()

    def format_data(self, data:dict[str, Any]):
        if "status" in data:
            logging.info(data["status"])
            return None
        
        if "error" in data:
            logging.info(data["error"])
            return None
        
        df = pd.DataFrame()
        df["Timestamp"], df["Price"] = list(zip(*data["prices"]))
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="ms", utc=True)

        return df

    def get_cached(self, conn:sqlite3.Connection, tick:str, params:dict):
        df:pd.DataFrame = pd.read_sql("""
            SELECT Price, Timestamp FROM t_Cache
            WHERE Params = ? AND Tick = ? AND Expiration >= CURRENT_TIMESTAMP
        """, conn, params=(jdumps(params), tick), parse_dates={"Timestamp" : {"format" : "ISO8601"}})

        if df.empty:
            logging.info("Expired or empty")
            return None
        
        logging.info("Cache hit!")
        return df

    def cache_data(self, conn:sqlite3.Connection, tick:str, params:dict, data:pd.DataFrame|None):
        if data is None: return

        data["Expiration"] = datetime.now(timezone.utc) + timedelta(seconds=self.expiration)

        data["Params"] = jdumps(params)
        data["Tick"] = tick

        data.to_sql("t_Cache", conn, if_exists="append", index=False)
        logging.info("Cached!")

    @override
    def get(self, tick, params):
        with sqlite3.connect(self.cache_db) as conn:
            self.update_db(conn)

            # Check if data with these params are in db
            #   If yes: Return those
            #   If not:
            #       Fetch
            #       Save to db
            #   Return

            if (d := self.get_cached(conn, tick, params)) is not None:
                return d

            data = self.fetch_data(params)
            data = self.format_data(data)
            self.cache_data(conn, tick, params, data)

            if data is None:
                return None

            return data[["Price", "Timestamp"]]

class ShareFetcher(Fetcher):
    @override
    def get(self, tick, params) -> pd.DataFrame:
        return None


if __name__ == "__main__":
    tick = "ethereum"
    url = f"https://api.coingecko.com/api/v3/coins/{tick}/market_chart"
    params = {"vs_currency":"usd", "days":5}
    f = CryptoFetcher(url, "cache.db", log_level=logging.INFO)

    df = f.get(tick, params)
    print(df.head())
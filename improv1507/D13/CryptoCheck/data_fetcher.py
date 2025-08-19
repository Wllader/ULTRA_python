from abc import ABC, abstractmethod
from typing import Any, override
import pandas as pd
import requests

import sqlite3


class Fetcher(ABC):
    def __init__(self, api_endpoint:str, cache_db_path:str, expiration_s:int=30):
        super().__init__()

        self.endpoint = api_endpoint
        self.cache_db = cache_db_path
        self.expiration = expiration_s

    @abstractmethod
    def get(self, tick, params) -> pd.DataFrame:
        pass

    def init_db(self, conn:sqlite3.Connection):
        cursor = conn.cursor()

        # Create table if not exists t_cache...

        cursor.execute("CREATE INDEX IF NOT EXISTS idx_cache_tick ON t_Cache(Tick)")



    def update_db(self, conn:sqlite3.Connection):
        self.init_db(conn)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM t_Cache WHERE Expiration < CURRENT_TIMESTAMP")


class CryptoFetcher(Fetcher):
    def fetch_data(self, params) -> dict[str, Any]:
        print("Fetching!")
        response = requests.get(self.endpoint, params)

        return response.json()
    
    def format_data(self, data:dict[str, Any]):
        if "status" in data:
            print(data["status"])
            return None
        
        if "error" in data:
            print(data["error"])
            return None
        
        df = pd.DataFrame()
        df["Timestamp"], df["Price"] = list(zip(*data["prices"]))
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="ms")

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

        data = self.fetch_data(params)
        data = self.format_data(data)

        if data is None:
            return None
        
        return data
    
class ShareFetcher(Fetcher):
    @override
    def get(self, tick, params) -> pd.DataFrame:
        pass
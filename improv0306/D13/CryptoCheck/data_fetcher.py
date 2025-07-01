from abc import ABC, abstractmethod
from typing import override, Any
import pandas as pd
import requests

import sqlite3

class Fetcher(ABC):
    def __init__(self, api_endpoint:str, cache_db:str):
        super().__init__()

        self.endpoint = api_endpoint #todo Check Template-strings
        self.cache_db = cache_db

    @abstractmethod
    def get(self, tick, params) -> pd.DataFrame:
        pass

    def init_db(self, conn:sqlite3.Connection):
        cursor = conn.cursor()

        cursor.execute("""

        """)

class CryptoFetcher(Fetcher):
    def fetch_data(self, params):
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
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="ms") #!

        return df

    @override
    def get(self, tick, params):


        data = self.fetch_data(params)
        data = self.format_data(data)

        return data #!

class ShareFetcher(Fetcher):
    @override
    def get(self, tick, params) -> pd.DataFrame:
        pass
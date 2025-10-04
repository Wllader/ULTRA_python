from abc import ABC, abstractmethod
from typing import Any, override
import pandas as pd, requests, logging
import sqlite3


class Fetcher(ABC):
    def __init__(self, api_endpoint:str, cache_db_path:str, expiration_s:int=30):
        super().__init__()

        self.endpoint = api_endpoint
        self.logger =logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def get(self, tick, params) -> pd.DataFrame:
        pass

    def init_db(self, conn:sqlite3.Connection):
        ...


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
        ...

    def get_cached(self, conn:sqlite3.Connection, tick:str, params:dict):
        ...

    


    @override
    def get(self, tick, params) -> pd.DataFrame|None:
        # Check if data with these params ar in db
        # If yes: Return those (*format)
        # If not:
        #   Fetch
        #   Format
        #   Save to db
        #   Return


        data = self.fetch_data(params)
        data = self.format_data(data)

        return data
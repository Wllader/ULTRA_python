from abc import ABC, abstractmethod
from typing import Any, override
import pandas as pd, requests, logging
import sqlite3


class Fetcher(ABC):
    def __init__(self, api_endpoint:str, cache_db_path:str, expiration_s:int=30):
        super().__init__()

        self.cache_db = cache_db_path
        self.expiration = expiration_s
        self.endpoint = api_endpoint
        self.logger = logging.getLogger(self.__class__.__name__)

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
                Exp DATETIME NOT NULL  
            )
        """)

        cursor.execute("CREATE INDEX IF NOT EXISTS idx_cache_tick ON t_Cache(Tick)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_cache_params ON t_Cache(Params)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_cache_exp ON t_Cache(Exp)")

        self.logger.info("Database connection initialized")


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
        df = pd.DataFrame()
        df["Timestamp"], df["Price"] = zip(*data["prices"])
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="ms")

        self.logger.info("Formatted!")
        return df


    @override
    def get(self, tick, params) -> pd.DataFrame|None:
        # todo:
        # Check if data with these params are in db:
        # If yes: Return those (formatted?)
        # If not:
        #   Fetch from remote API
        #   Format
        #   Save to DB
        #   Return


        data = self.fetch_data(params)
        if not self.check_data(data): return
        data = self.format_data(data)

        return data




from abc import ABC, abstractmethod
from typing import Any, override
import pandas as pd, requests, logging, sqlite3

class Fetcher(ABC):
    def __init__(self, api_endpoint:str):
        super().__init__()

        self.endpoint = api_endpoint
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def get(self, tick, params) -> pd.DataFrame|None:
        pass

    def init_db(self, conn:sqlite3.Connection):
        ... #todo
        # ID, Tick, Price, Timestamp, Params (TEXT JSON), Expiration


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
        #todo
        # Check if data with these params are in db
        # If yes: Return those (formatted?)
        # If not:
        #   Fetch from remote API (Coingecko)
        #   Format
        #   Save to DB
        #   Return
        data = self.fetch_data(params)
        if not self.check_data(data): return
        data = self.format_data(data)

        return data


class ShareFetcher(Fetcher):
    @override
    def get(self): pass
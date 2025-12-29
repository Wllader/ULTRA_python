from abc import ABC, abstractmethod
from typing import Any, override
import pandas as pd, requests, logging, sqlite3


class Fetcher(ABC):
    def __init__(self, cache_db_path:str=None, expiration_s:int=30):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.cache_db = cache_db_path
        self.expiration = expiration_s

        if self.cache_db is None: return
        with sqlite3.connect(self.cache_db) as conn:
            self.init_db(conn)

    @abstractmethod
    def get(self, tick, params) -> pd.DataFrame|None:
        pass

    def init_db(self, conn:sqlite3.Connection):
        # Define table t_Cache:
        #   - Id (PK)
        #   - Tick, Price, Timestamp
        #   - Params (TEXT)
        #   - Exp (DATETIME)
        pass

    def delete_expired(self, conn:sqlite3.Connection):
        # Check for expired rows in t_Cache:
        #   cond: CURRENT_TIMESTAMP >= Exp
        #   DELETE FROM table WHERE cond
        pass


class CryptoFetcher(Fetcher):
    def fetch_data(self, endpoint, params) -> dict[str, Any]:
        self.logger.info("Fetching!")
        response = requests.get(endpoint, params)
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
        # Check if data with these params are in DB
        # If yes: Return those (formatted already)
        # If not:
        #  Fetch from remote API (Coingecko)
        #  Check
        #  Format
        #  Save to DB
        #  Return

        endpoint = f"https://api.coingecko.com/api/v3/coins/{tick}/market_chart"

        data = self.fetch_data(endpoint, params)
        if not self.check_data(data): return None
        data = self.format_data(data)

        return data
    
class ShareFetcher(Fetcher):
    @override
    def get(self): pass

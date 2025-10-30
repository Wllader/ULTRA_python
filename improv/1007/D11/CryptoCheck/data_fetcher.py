from abc import ABC, abstractmethod
from typing import Any, override
import pandas as pd, requests, logging


class Fetcher(ABC):
    def __init__(self, api_endpoint:str):
        super().__init__()

        self.endpoint = api_endpoint
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def get(self, tick, params) -> pd.DataFrame:
        pass


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
        data = self.fetch_data(params)
        if not self.check_data(data): return
        data = self.format_data(data)

        return data




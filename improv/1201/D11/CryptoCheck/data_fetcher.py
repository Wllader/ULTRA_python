from abc import ABC, abstractmethod
from typing import Any, override
import pandas as pd, requests, logging


class Fetcher(ABC):


    @abstractmethod
    def get(self, tick, params) -> pd.DataFrame|None:
        pass


class CryptoFetcher(Fetcher):
    ...
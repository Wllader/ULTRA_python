from abc import ABC, abstractmethod
from typing import Any, override
import pandas as pd, requests, logging, sqlite3
from json import dumps as jdumps
from datetime import datetime, timedelta, timezone


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
        
        conn.execute("""
            CREATE TABLE IF NOT EXISTS t_Cache (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Tick TEXT NOT NULL,
                Price REAL NOT NULL,
                Timestamp DATETIME NOT NULL,
                Params TEXT NOT NULL,
                Exp DATETIME NOT NULL         
            )
        """)

        conn.execute("CREATE INDEX IF NOT EXISTS idx_cache_tick ON t_Cache(Tick)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_cache_params ON t_Cache(Params)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_cache_exp ON t_Cache(Exp)")

        self.logger.info("Database connection initialiazed")

    def delete_expired(self, conn:sqlite3.Connection):
        # Check for expired rows in t_Cache:
        #   cond: CURRENT_TIMESTAMP >= Exp
        #   DELETE FROM table WHERE cond
        cursor = conn.execute("SELECT COUNT() FROM t_Cache WHERE Exp < CURRENT_TIMESTAMP")
        n = cursor.fetchone()[0]

        if n > 0:
            conn.execute("DELETE FROM t_Cache WHERE Exp < CURRENT_TIMESTAMP")
            self.logger.info(f"Pruned {n} expired records")


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
    
    def get_cached(self, conn:sqlite3.Connection, tick:str, params:dict[str, Any]) -> pd.DataFrame|None:
        df:pd.DataFrame = pd.read_sql("""
            SELECT Price, Timestamp FROM t_Cache
            WHERE Params = ? AND Tick = ? AND Exp >= CURRENT_TIMESTAMP
        """, conn, params=(jdumps(params, sort_keys=True), tick), parse_dates={"Timestamp" : {"format" : "ISO8601"}})

        if df.empty:
            self.logger.info("Cache miss: Expired or empty!")
            return None
        
        self.logger.info("Cache hit!")
        return df

    def cache_data(self, conn:sqlite3.Connection, tick:str, params:dict[str, Any], data:pd.DataFrame|None) -> bool:
        if data is None or data.empty: return False

        data["Exp"] = datetime.now(timezone.utc) + timedelta(seconds=self.expiration)

        data["Params"] = jdumps(params, sort_keys=True)
        data["Tick"] = tick

        data.to_sql("t_Cache", conn, index=False, if_exists="append")
        self.logger.info(f"Cached {len(data)} items!")
        return True

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
        def _get():
            data = self.fetch_data(endpoint, params)
            if not self.check_data(data): return None
            data = self.format_data(data)
            return data

        if self.cache_db is None:
            data = _get()
            return data
        
        with sqlite3.connect(self.cache_db) as conn:
            self.delete_expired(conn)
            if (d := self.get_cached(conn, tick, params)) is not None:
                return d
    
            data = _get()
            if self.cache_data(conn, tick, params, data):
                return data[["Price", "Timestamp"]]
            
            return None

class ShareFetcher(Fetcher):
    @override
    def get(self): pass

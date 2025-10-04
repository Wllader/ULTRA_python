from fastapi import FastAPI
from data_fetcher import CryptoFetcher

app = FastAPI()

@app.get("/")
def test():
    return {"message": "Hello world!"}


@app.get("/test2/{item}")
def test2(item:str, color:str="red", count:int=1):
    return {
        "item": item,
        "color": color,
        "count": count
    }

@app.get("/coin/{coin_id}")
def get_coin(coin_id:str, vs_currency:str="usd", days:int=5):
    fetcher = CryptoFetcher("cache.db")
    return fetcher.get_json(coin_id, {"days":days, "vs_currency":vs_currency})
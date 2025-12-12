import requests, json
import pandas as pd
from matplotlib import pyplot as plt
import sqlite3


# url = "https://api.coingecko.com/api/v3/simple/price"
# params = {
#     "vs_currencies" : "usd,czk",
#     "ids" : "bitcoin,ethereum"
# }

id = "doge"
url = f"https://api.coingecko.com/api/v3/coins/{id}/market_chart"
params = {
    "vs_currency" : "usd",
    "days" : 5
}

response = requests.get(url, params)
data = response.json()

with open(f"files/{id}_cache.json", "w") as f:
    json.dump(data, f, indent=4)


# loaded_data = None
# with open(f"files/{id}_cache.json", "r") as f:
#     loaded_data = json.load(f)

# print(type(loaded_data), loaded_data.keys(), loaded_data, sep="\n--\n")

df = pd.DataFrame()
df["Timestamp"], df["Price"] = zip(*data["prices"])
df["MarketCap"] = list(zip(*data["market_caps"]))[1]
df["TotalVolume"] = list(zip(*data["total_volumes"]))[1]
df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="ms")

df.to_json(f"files/{id}_cache_v2.json", index=False, indent=4)


# df = pd.read_json(f"files/{id}_cache_v2.json")
# print(df.head())


with sqlite3.connect("files/crypto_cache.db") as conn:
    df.to_sql(f"{id.capitalize()}", conn, index=False, if_exists="replace")
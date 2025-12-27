import requests, json
import pandas as pd
import sqlite3

id = "doge"
url = f"https://api.coingecko.com/api/v3/coins/{id}/market_chart"
params = {
    "vs_currency" : "usd",
    "days" : 5
}

response = requests.get(url, params)

data = response.json()

with open(f"files/{id}_cache.json", "w") as f:
    json.dump(data, f)


# loaded_data = None
# with open(f"files/{id}_cache.json", "r") as f:
#     loaded_data = json.load(f)

# print(type(loaded_data), loaded_data.keys())


df = pd.DataFrame()
df["Timestamp"], df["Price"] = zip(*data["prices"])
_, df["MarketCap"] = zip(*data["market_caps"])
_, df["TotalVolume"] = zip(*data["total_volumes"])

df.to_json(f"files/{id}_cache_v2.json", index=False)

# df = pd.read_json(f"files/{id}_cache_v2.json")
# print(df.head())

with sqlite3.connect("files/crypto_cache.db") as conn:
    df.to_sql(f"{id.capitalize()}", conn, index=False, if_exists="replace")
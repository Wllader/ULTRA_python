import requests, pandas as pd
import matplotlib.pyplot as plt
import json
import sqlite3

coin_id = "bitcoin"
params = {
    "vs_currency" : "usd",
    "days" : 1
}

url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame()
df["Timestamp"], df["Price"] = zip(*data["prices"])
df["MarketCap"] = list(zip(*data["market_caps"]))[1]
df["TotalVolume"] = list(zip(*data["total_volumes"]))[1]
df["Datetime"] = pd.to_datetime(df["Timestamp"], unit="ms")

df.insert(len(df.columns) - 1, "Timestamp", df.pop("Timestamp"))


# plt.plot(df["Datetime"], df["Price"])
# plt.title(f"{coin_id.capitalize()} price Trend")
# plt.xlabel("Date")
# plt.ylabel(f"Price ({params['vs_currency'].upper()})")
# plt.grid(True)
# plt.tight_layout()
# plt.show()


# with open(f"files/{coin_id}_cache.json", "w") as f:
#     json.dump(data, f)


# loaded_data = None
# with open(f"files/{coin_id}_cache.json", "r") as f:
#     loaded_data = json.load(f)

# print(type(loaded_data), loaded_data.keys())

# df.to_json(f"files/{coin_id}_dfCache.json")

# df = pd.read_json(f"files/{coin_id}_dfCache.json", convert_dates=["Datetime"], keep_default_dates=False)

# print(df.head())


with sqlite3.connect("files/crypto_cache.db") as connection:
    cursor = connection.cursor()

    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS t_price (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vch_coin TEXT NOT NULL,
            f_usd REAL NOT NULL,
            timestamp DATETIME NOT NULL,
            time_edited DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Insert data into table
    for row in df.itertuples():
        cursor.execute("INSERT INTO t_price (vch_coin, f_usd, timestamp) VALUES (?, ?, ?)", (coin_id, row.Price, row.Datetime.__str__()))


import requests
import pandas as pd
from datetime import datetime, date
from typing import Literal

# url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

coin_id = "ethereum"
days = 7
vs_currency = "usd"

url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency={vs_currency}&days={days}"
response = requests.get(url)

data = response.json()


def tmstp2time(timestamp, type:Literal["date", "time", "datetime"] = "datetime"):
    s = timestamp / 1000
    match type:
        case "date":
            d = date.fromtimestamp(s)
        case "time":
            d = datetime.fromtimestamp(s)
            d = d.strftime("%H:%M:%S")
        case "datetime":
            d = datetime.fromtimestamp(s)

    return d

df = pd.DataFrame()
df["Timestamp"], df["Price"] = list(zip(*data["prices"]))
df["MarketCap"] = list(zip(*data["market_caps"]))[1]
df["TotalVolume"] = list(zip(*data["total_volumes"]))[1]

df["Date"] = [ tmstp2time(ts, "date") for ts in df["Timestamp"] ]
df["Time"] = [ tmstp2time(ts, "time") for ts in df["Timestamp"] ]
# df["Datetime"] = [ tmstp2time(ts) for ts in df["Timestamp"] ]
df["Datetime"] = pd.to_datetime(df["Timestamp"], unit="ms")

df.insert(len(df.columns) - 1, "Timestamp", df.pop("Timestamp"))

print(df)


import matplotlib.pyplot as plt

plt.plot(df.Datetime, df.Price)
plt.title(f"{coin_id.capitalize()} price trend")
plt.xlabel("Date")
plt.ylabel("USD")
plt.grid()
# plt.show()

import json

# with open(f"files/{coin_id}_cache.json", "w") as f:
#     json.dump(data, f)

# with open(f"files/{coin_id}_cache.json", "r") as f:
#     loaded_data = json.load(f)


df.to_json(f"files/{coin_id}_cache.json")


# loaded_data = pd.read_json(f"files/{coin_id}_cache.json", convert_dates=["Date", "Datetime"], keep_default_dates=False)
# print(loaded_data)

import sqlite3

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
        cursor.execute("INSERT INTO t_price (vch_coin, f_usd, timestamp) VALUES (?, ?, ?)", (coin_id, row.Price, row.Timestamp))

    connection.commit()

    # Querry into a table:
    # for row in cursor.execute("SELECT * FROM t_price LIMIT 5"):
    #     print(row)





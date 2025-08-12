import requests, json
import pandas as pd
import matplotlib.pyplot as plt

id = "bitcoin"

params = {
    "vs_currency" : "czk",
    "days" : 5
}

url = f"https://api.coingecko.com/api/v3/coins/{id}/market_chart"
response = requests.get(url, params)

data = response.json()


# with open(f"files/{id}_cache.json", "w") as f:
#     json.dump(data, f)


# loaded_data = None
# with open(f"files/{id}_cache.json", "r") as f:
#     loaded_data = json.load(f)

# print(type(loaded_data), loaded_data.keys())

df = pd.DataFrame()
df["Timestamp"], df["Price"] = zip(*data["prices"])
df["MarketCap"] = list(zip(*data["market_caps"]))[1]
df["TotalVolume"] = list(zip(*data["total_volumes"]))[1]
df["DateTime"] = pd.to_datetime(df["Timestamp"], unit="ms")


df.insert(len(df.columns) - 1, "Timestamp", df.pop("Timestamp"))

df.to_json(f"files/{id}_dfCache.json", index=False)


plt.plot(df["DateTime"], df["Price"])
plt.title(f"{id.capitalize()} price Trend")
plt.xlabel("Date")
plt.ylabel(f"Price ({params["vs_currency"].upper()})")
plt.grid(True)
plt.tight_layout()
plt.show()

# print(df.head())

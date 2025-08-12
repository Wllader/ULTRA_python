import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_json("files/bitcoin_dfCache.json", keep_default_dates=False, convert_dates=["DateTime"])
print(df.head())


# plt.plot(df["DateTime"], df["Price"])
# plt.title(f"Price Trend")
# plt.xlabel("Date")
# plt.ylabel(f"Price")
# plt.grid(True)
# plt.tight_layout()
# plt.show()
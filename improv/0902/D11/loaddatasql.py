import pandas as pd
import matplotlib.pyplot as plt
import sqlite3


with sqlite3.connect("files/crypto_cache.db") as conn:
    df:pd.DataFrame = pd.read_sql("SELECT * FROM Bitcoin", conn)

print(df.head())


plt.plot(df["Timestamp"], df["Price"])
plt.title(f"Price Trend")
plt.xlabel("Date")
plt.ylabel(f"Price")
plt.grid(True)
plt.tight_layout()
plt.show()
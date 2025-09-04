import sqlite3
import pandas as pd
from matplotlib import pyplot as plt

with sqlite3.connect("files/crypto_cache.db") as connection:
    df = pd.read_sql("SELECT * FROM t_price WHERE vch_coin = 'ethereum'", connection)


df.timestamp = pd.to_datetime(df.timestamp, unit="ms")


df.plot(x="timestamp", y="f_usd", kind="line", title="Price over time")
plt.show()
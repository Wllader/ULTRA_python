import sqlite3, pandas as pd

with sqlite3.connect("files/crypto_cache.db") as connection:
    df = pd.read_sql(
        "SELECT * FROM t_price WHERE vch_coin = 'bitcoin' AND timestamp >= '2025-06-25 20:00:00' ORDER BY timestamp desc",
        connection,
        parse_dates={"timestamp" : "ISO8601", "time_edited" : "ISO8601"})

print(df)
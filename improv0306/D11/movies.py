import pandas as pd, sqlite3

# Create DB for movies and their Directors
with sqlite3.connect("files/movies.db") as conn:
    cursor = conn.cursor()

    # Enable foreign keys in SQLite
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("DROP TABLE IF EXISTS t_Movie")
    cursor.execute("DROP TABLE IF EXISTS t_Director")

    # Create directors table:
    ...

    # Create Movies table:
    ...



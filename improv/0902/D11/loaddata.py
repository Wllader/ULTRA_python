import sqlite3
import pandas as pd

queries = [
    "SELECT * FROM t_Director;",


    "SELECT * FROM t_Director WHERE d_Birth > '1950-00-00';",

    "SELECT * FROM t_Movie WHERE d_Premiere < '1980-00-00';",

    """SELECT *
    FROM t_Director d INNER JOIN t_Movie m
    ON d.Id == m.fk_DirectorId
    WHERE m.d_Premiere > '2023-00-00';""",

    """SELECT d.Id AS DirectorId, d.vch_FirstName, d.vch_LastName, m.vch_Title, m.d_Premiere, m.Id AS MovieId
    FROM t_Director d INNER JOIN t_Movie m
    ON d.Id == m.fk_DirectorId
    WHERE m.d_Premiere > '2000-00-00'
        AND m.vch_Title LIKE '%d'
    ORDER BY m.d_Premiere DESC;"""
]


with sqlite3.connect("files/Movies.db") as conn:
    cursor = conn.cursor()

    df = pd.read_sql(queries[4], conn)

print(df)
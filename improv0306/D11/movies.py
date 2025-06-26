import pandas as pd, sqlite3


directors = [
    ('Steven', 'Spielberg', '1946-12-18'),
    ('Martin', 'Scorsese', '1942-11-17'),
    ('Christopher', 'Nolan', '1970-07-30'),
    ('Kathryn', 'Bigelow', '1951-11-27'),
    ('Quentin', 'Tarantino', '1963-03-27')
]

movies = [
    # Steven Spielberg (DirectorId = 1)
    ("Jaws", "1975-06-20", 1),
    ("Close Encounters of the Third Kind", "1977-11-16", 1),
    ("Raiders of the Lost Ark", "1981-06-12", 1),
    ("E.T. the Extra-Terrestrial", "1982-06-11", 1),
    ("Jurassic Park", "1993-06-11", 1),
    ("Schindler's List", "1993-12-15", 1),
    ("Saving Private Ryan", "1998-07-24", 1),
    ("Catch Me If You Can", "2002-12-25", 1),
    ("Lincoln", "2012-11-09", 1),
    ("The Fabelmans", "2022-11-11", 1),

    # Martin Scorsese (DirectorId = 2)
    ("Mean Streets", "1973-10-02", 2),
    ("Taxi Driver", "1976-02-08", 2),
    ("Raging Bull", "1980-11-14", 2),
    ("Goodfellas", "1990-09-19", 2),
    ("Casino", "1995-11-22", 2),
    ("The Departed", "2006-10-06", 2),
    ("Shutter Island", "2010-02-19", 2),
    ("The Wolf of Wall Street", "2013-12-25", 2),
    ("Silence", "2016-12-23", 2),
    ("Killers of the Flower Moon", "2023-10-20", 2),

    # Christopher Nolan (DirectorId = 3)
    ("Memento", "2000-10-11", 3),
    ("Insomnia", "2002-05-24", 3),
    ("Batman Begins", "2005-06-15", 3),
    ("The Prestige", "2006-10-20", 3),
    ("The Dark Knight", "2008-07-18", 3),
    ("Inception", "2010-07-16", 3),
    ("Interstellar", "2014-11-07", 3),
    ("Dunkirk", "2017-07-21", 3),
    ("Tenet", "2020-08-26", 3),
    ("Oppenheimer", "2023-07-21", 3),

    # Kathryn Bigelow (DirectorId = 4)
    ("The Loveless", "1981-10-01", 4),
    ("Near Dark", "1987-10-02", 4),
    ("Blue Steel", "1990-03-16", 4),
    ("Point Break", "1991-07-12", 4),
    ("Strange Days", "1995-10-13", 4),
    ("K-19: The Widowmaker", "2002-07-19", 4),
    ("The Hurt Locker", "2008-10-10", 4),
    ("Zero Dark Thirty", "2012-12-19", 4),
    ("Detroit", "2017-07-28", 4),

    # Quentin Tarantino (DirectorId = 5)
    ("Reservoir Dogs", "1992-10-23", 5),
    ("Pulp Fiction", "1994-10-14", 5),
    ("Jackie Brown", "1997-12-25", 5),
    ("Kill Bill: Volume 1", "2003-10-10", 5),
    ("Kill Bill: Volume 2", "2004-04-16", 5),
    ("Death Proof", "2007-05-31", 5),
    ("Inglourious Basterds", "2009-08-21", 5),
    ("Django Unchained", "2012-12-25", 5),
    ("The Hateful Eight", "2015-12-25", 5),
    ("Once Upon a Time in Hollywood", "2019-07-26", 5)
]


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



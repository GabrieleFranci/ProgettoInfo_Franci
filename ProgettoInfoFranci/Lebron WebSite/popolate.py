import sqlite3

conn = sqlite3.connect("lebron.db")
c = conn.cursor()

# Create tables
c.execute('''
    CREATE TABLE IF NOT EXISTS stats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        season TEXT,
        team TEXT,
        games_played INTEGER,
        points_per_game REAL,
        rebounds_per_game REAL,
        assists_per_game REAL,
        steals_per_game REAL,
        blocks_per_game REAL
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS game (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        game_date TEXT,
        opponent TEXT,
        home_away TEXT,
        result TEXT,
        points INTEGER,
        assists INTEGER,
        rebounds INTEGER,
        location TEXT
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS highlight (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        video_url TEXT,
        category TEXT,
        event_date TEXT
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS quote (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quote TEXT,
        source TEXT,
        quote_year INTEGER
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS career_event (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_date TEXT,
        description TEXT
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS comment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        content TEXT,
        comment_date TEXT DEFAULT CURRENT_TIMESTAMP
    )
''')

# Insert data
stats_data = [
    (2003, 'Cavs', 82, 20.9, 5.5, 5.9, 1.6, 0.7),
    (2004, 'Cavs', 80, 27.2, 7.4, 7.2, 1.6, 0.8),
    (2005, 'Cavs', 81, 31.4, 7.0, 6.6, 1.6, 0.8),
    (2006, 'Cavs', 79, 27.3, 6.7, 6.0, 1.6, 0.8),
    (2007, 'Cavs', 78, 30.0, 7.9, 7.2, 1.6, 0.7),
    (2008, 'Cavs', 81, 28.4, 7.6, 7.2, 1.8, 0.8),
    (2009, 'Cavs', 81, 29.7, 8.6, 8.3, 1.6, 0.7),
    (2010, 'Heat', 79, 26.7, 7.5, 7.0, 1.6, 0.7),
    (2011, 'Heat', 79, 27.1, 6.9, 6.2, 1.6, 0.8),
    (2012, 'Heat', 74, 26.8, 8.0, 7.3, 1.6, 0.6),
    (2013, 'Heat', 75, 25.1, 6.9, 7.1, 1.6, 0.5),
    (2014, 'Heat', 77, 27.1, 6.9, 6.4, 1.5, 0.3),
    (2015, 'Cavs', 76, 25.3, 7.4, 6.8, 1.4, 0.5),
    (2016, 'Cavs', 76, 24.8, 7.5, 8.7, 1.4, 0.5),
    (2017, 'Cavs', 74, 26.4, 8.6, 8.7, 1.2, 0.5),
    (2018, 'Lakers', 82, 27.5, 8.3, 8.3, 1.2, 0.5),
    (2019, 'Lakers', 71, 25.3, 7.8, 10.2, 1.2, 0.5),
    (2020, 'Lakers', 82, 25.0, 7.7, 10.2, 1.2, 0.5),
    (2021, 'Lakers', 56, 25.0, 7.7, 10.2, 1.2, 0.5),
    (2022, 'Lakers', 78 , 27.4 , 8 , 9.3 , 1.0 , 0.5 ),
    (2023,'Lakers',80 , 26.9 , 8 , 9.6 , 1.0 , 0.5 ),
]
c.executemany("INSERT INTO stats (season, team, games_played, points_per_game, rebounds_per_game, assists_per_game, steals_per_game, blocks_per_game) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", stats_data)

games_data = [
    ("2023-11-05", "Warriors", "Home", "Win", 34, 8, 9, "LA"),
    ("2023-11-10", "Celtics", "Away", "Lose", 28, 7, 11, "Boston"),
    ("2023-11-15", "Bucks", "Home", "Win", 31, 10, 6, "LA"),
    ("2023-11-20", "Nets", "Away", "Win", 26, 6, 7, "Brooklyn"),
    ("2023-11-25", "Suns", "Home", "Win", 38, 10, 12, "LA"),
    ("2023-12-01", "Knicks", "Away", "Lose", 24, 5, 10, "New York"),
    ("2023-12-05", "Heat", "Home", "Win", 33, 7, 8, "LA"),
    ("2023-12-10", "Spurs", "Away", "Win", 29, 8, 6, "San Antonio"),
    ("2023-12-15", "Clippers", "Home", "Win", 35, 11, 7, "LA"),
    ("2011-02-03", "Hornets", "Away", "Win", 61, 8, 6, "Charlotte"),
    ("2012-03-04", "Thunder", "Home", "Win", 50, 7, 8, "Miami"),
    ("2013-04-05", "Bulls", "Away", "Lose", 32, 9, 5, "Chicago"),
    ("2014-05-01", "Pacers", "Home", "Win", 45, 10, 12, "Miami"),
    ("2015-06-16", "Warriors", "Away", "Win", 40, 10, 5, "Golden State"),
    ("2016-07-19", "Celtics", "Home", "Win", 37, 8, 9, "Cleveland"),
    ("2017-08-10", "Raptors", "Away", "Win", 30, 6, 7, "Toronto"),
]
c.executemany("INSERT INTO game (game_date, opponent, home_away, result, points, assists, rebounds, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", games_data)

highlight_data = [
    ("Schiacciata incredibile", "Schiacciata in contropiede contro i Warriors", "https://video_url1", "Schiacciata", "2023-11-05"),
    ("Triple decisiva", "Tripla decisiva contro i Celtics", "https://video_url2", "Triple", "2023-11-10"),
    ("Blocco spettacolare", "Blocco spettacolare su Antetokounmpo", "https://video_url3", "Blocco", "2023-11-15"),
    ("Assist no-look", "Assist no-look a Davis", "https://video_url4", "Assist", "2023-11-20"),
    ("33 punti nel primo tempo", "33 punti nel primo tempo contro i Suns", "https://video_url5", "Punti", "2023-11-25"),
    ("Alley-oop con Russell", "Alley-oop con Russell contro i Knicks", "https://video_url6", "Alley-oop", "2023-12-01"),
    ("Tripla da metà campo", "Tripla da metà campo contro gli Heat", "https://video_url7", "Tripla", "2023-12-05"),
    ("10 assist", "10 assist nel primo tempo contro gli Spurs", "https://video_url8", "Assist", "2023-12-10"),
    ("Dominio a rimbalzo", "Dominio a rimbalzo contro i Clippers", "https://video_url9", "Rimbalzo", "2023-12-15"),
    ("Game-winner", "Game-winner contro i Bulls", "https://video_url10", "Game-winner", "2023-12-20")
]
c.executemany("INSERT INTO highlight (title, description, video_url, category, event_date) VALUES (?, ?, ?, ?, ?)", highlight_data)

quote_data = [
    ("You have to be able to accept failure to get better.", "LeBron James", 2010),
    ("I’m going to use all my tools, my God-given ability, and make the best life I can with it.", "LeBron James", 2008),
    ("Dream as if you'll live forever. Live as if you'll die today.", "LeBron James", 2006),
    ("The only thing I fear is fear itself.", "LeBron James", 2009),
    ("I like criticism. It makes you strong.", "LeBron James", 2011),
    ("You can’t be afraid to fail. It’s the only way you succeed.", "LeBron James", 2013),
    ("I’m not afraid of anyone, I’m just focused on my game.", "LeBron James", 2012),
    ("I love to compete. That’s the one thing I can control.", "LeBron James", 2014),
    ("You don’t play against opponents. You play against the game of basketball.", "LeBron James", 2016),
    ("I’m the best player in the world. I don’t care what anybody says.", "LeBron James", 2015)
]
c.executemany("INSERT INTO quote (quote, source, quote_year) VALUES (?, ?, ?)", quote_data)

event_data = [
    ("2003-06-26", "Draftato dai Cleveland Cavaliers"),
    ("2010-07-08", "Passaggio ai Miami Heat"),
    ("2016-06-19", "Vince il titolo NBA con i Cavaliers"),
    ("2018-07-01", "Passaggio ai Los Angeles Lakers"),
    ("2020-10-11", "Vince il quarto titolo NBA con i Lakers"),
    ("2021-03-12", "Supera Kobe Bryant nella classifica marcatori NBA"),
    ("2022-06-01", "Primo in classifica nei punti totali per una stagione regolare NBA"),
    ("2023-01-05", "Passa la soglia dei 30.000 punti in carriera"),
    ("2024-05-02", "All-Star per il 19° anno consecutivo"),
    ("2025-01-20", "Raggiunge i 40.000 punti nella sua carriera")
]
c.executemany("INSERT INTO career_event (event_date, description) VALUES (?, ?)", event_data)

comment_data = [
    ("Gabriele Franci", "LeBron è il GOAT!"),
    ("Danilo Gallinari", "Incredibile la sua evoluzione nel corso degli anni!"),
    ("Luka Modric", "Il miglior giocatore che abbia mai visto!"),
    ("DJ Khaled", "Another one for the KING👑!"),
    ("Jakidale", "Non c'è nessuno come lui in NBA, iscrivetevi al mio canale telegram."),
    ("Matteo Pelusi", "Ogni partita è un capolavoro."),
    ("Papa Francesco", "Il suo impatto sul gioco è immenso."),
    ("King von", "Non vedo l'ora di vedere il prossimo campionato!"),
    ("Davide Cantelli", "Inarrestabile, anche all'età che ha."),
    ("Ivan Grieco", "La sua leadership è un esempio per tutti!")
]
c.executemany("INSERT INTO comment (username, content) VALUES (?, ?)", comment_data)

conn.commit()
conn.close()

print("Database creato e popolato con successo.")

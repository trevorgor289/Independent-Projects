import sqlite3, os
from indepth_scraper import DifficultyScore


URL = "https://boardgamegeek.com/browse/boardgame?sort=rank&rankobjecttype=subtype&rankobjectid=1&rank=14#14"
absolute_path = r"C:\Users\tgord\OneDrive\Documents\work\portfolio projects\SQlite databases"
os.chdir(absolute_path)
conn = sqlite3.connect("boardgames2.sqlite")
cur = conn.cursor()

# retrieving the difficulty ratings for all top 100 games and inserting into separate SQL table
difficulty = DifficultyScore(URL)
difficulty.get_links()
difficulty.retrieve_difficulty_score()
cur.execute('DROP TABLE IF EXISTS Difficulty')
cur.execute('''CREATE TABLE Difficulty (id integer PRIMARY KEY, title_id INTEGER, difficulty_score INTEGER)''')
conn.commit()
print('new table')
x = 1
for score in difficulty.difficulty_list:
    cur.execute('''INSERT INTO Difficulty (Difficulty_Score, title_id) VALUES (?,?)''', (score, x))
    x += 1
conn.commit()


# joining the game difficulty rating table with the game title and ratings table, and creating a new table with all information.
cur.execute('DROP TABLE IF EXISTS Game_Difficulty')
conn.commit()
cur.execute('DROP TABLE IF EXISTS All_Together')
cur.execute(
    '''CREATE TABLE All_Together 
    (id integer PRIMARY KEY, Game TEXT, Difficulty INTEGER, Geekratings INTEGER, Numvoters INTEGER)''')
cur.execute(
    '''SELECT Ratings.title2, Difficulty.difficulty_score, Ratings.Geekratings, Ratings.NumVoters FROM Difficulty 
    JOIN Ratings ON Difficulty.title_id = Ratings.id''')
rows = cur.fetchall()
for row in rows:
    print(row)
    cur.execute('''INSERT INTO All_Together (Game, Difficulty, Geekratings, Numvoters ) VALUES (?,?,?,?)''', (row[0], row[1], row[2], row[3]))

conn.commit()
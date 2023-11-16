import requests
from bs4 import BeautifulSoup
import os, sqlite3

URL = "https://boardgamegeek.com/browse/boardgame?sort=rank&rankobjecttype=subtype&rankobjectid=1&rank=14#14"
soup = BeautifulSoup(requests.get(URL).text, 'html.parser')
tsoup = soup.text
board_games = []
bg = []

# retrieving all names for top 100 board games..
anchor_tags = soup.find_all(name="a")
for tag in anchor_tags:
    board_games.append(tag.text)
bg = [string for string in board_games if len(string) > 0]
bg = bg[11:(len(bg) - 6)]

# retrieving ratings for each boardgame
scores = []
clean_scores = []
td_tag = soup.find_all(name="td", class_="collection_bggrating")
for item in td_tag:
    scores.append(item.text)
for score in scores:
    clean_scores.append(score.strip())
i = 0
clean_scores2 = []
while i < len(clean_scores):
    clean_scores2.append(clean_scores[i:i + 3])
    i += 3

# converting lists to dictionary
dict = {bg[i]: clean_scores2[i] for i in range(len(bg))}

# importing data to SQLite
absolute_path = r"C:\Users\tgord\OneDrive\Documents\work\portfolio projects\SQlite databases"
os.chdir(absolute_path)

conn = sqlite3.connect("boardgames2.sqlite")
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ratings')
cur.execute(
    '''CREATE TABLE Ratings (id integer PRIMARY KEY, title2 TEXT, Geekratings INTEGER, Averatings INTEGER, NumVoters INTEGER)''')

num_lst = []
for k, v in dict.items():
    for num in v:
        num_lst.append(num)
    cur.execute('''INSERT INTO Ratings (title2, Geekratings, Averatings, NumVoters) VALUES (?,?,?,?)''',
                (k, num_lst[0], (num_lst[1]), (num_lst[2])))
    num_lst = []
conn.commit()


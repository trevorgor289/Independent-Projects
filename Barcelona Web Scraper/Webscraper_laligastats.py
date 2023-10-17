import requests
from bs4 import BeautifulSoup
import pandas
import csv

URL = "https://www.espn.com/soccer/stats/_/league/ESP.1/view/scoring"

# Write your code below this line 👇

response = requests.get(URL)

soup = response.text

b_soup = BeautifulSoup(soup, "html.parser")


#
top_goalscorers = b_soup.find(name="div", class_="ResponsiveTable top-score-table")
players = b_soup.find(name="tbody", class_="Table__TBODY")
player = players.contents

#contents is what allows you to read the text on a single element

top_goalscorers_name = []
top_goalscorers_club = []
games = []
goals = []
my_dict = {}

for stat in player:
    name = stat.select(selector="a", class_='AnchorLink')
    name1 = name[0].contents
    name2 = name1[0]
    club = name[1].contents
    club1 = club[0]
    top_goalscorers_name.append(name2)
    top_goalscorers_club.append(club1)


for stat in player:
    stats = stat.select(selector="span", class_='tar')
    games_played = stats[2].contents
    games.append(games_played[0])
    goals_scored = stats[3].contents
    goals.append(goals_scored[0])

print(goals)


x = 0
for name in top_goalscorers_name:
    my_dict[name] = (top_goalscorers_club[x], games[x], goals[x])
    x += 1

{'name': {}}
#
with open("top_goalscorer_stats.txt", mode = "w", encoding="utf8") as file:
    x = 1
    for player, goals in my_dict.items():
        file.write(f"\n{x}. {player}\n   {goals}")
        x += 1




csvFile = open('test.csv', 'w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('Name', 'Club', 'Games Played', 'Goals Scored'))
    x = 0
    for i in range(50):
        writer.writerow((top_goalscorers_name[x], top_goalscorers_club[x],
                         games[x], goals[x]))
        x += 1
finally:
    csvFile.close()







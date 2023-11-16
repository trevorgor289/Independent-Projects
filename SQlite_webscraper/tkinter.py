from tkinter import *
import sqlite3, os
import tkinter

def button_clicked():

    absolute_path = r"C:\Users\tgord\OneDrive\Documents\work\portfolio projects\SQlite databases"
    os.chdir(absolute_path)
    conn = sqlite3.connect("boardgames2.sqlite")
    cur = conn.cursor()
    ranking = input.get()
    cur.execute(
        f'''SELECT All_Together.Game, All_Together.Difficulty, All_Together.Geekratings, All_Together.Numvoters FROM All_Together WHERE {ranking} = All_Together.id''')
    rows = cur.fetchall()
    print(rows)
    for row in rows:
        new_label.config(text=row[0])
        stats = Label(text=f"Difficulty: {row[1]}, GeekRating: {row[2]}, NumVoters: {row[3]}", font=("Arial", 12, "bold"))
        stats.grid(column=3, row=1)
        stats.config(padx=20, pady=20)

# creating a GUI program that will display game name and stats when the ranking out of top 100 is entered.

window = Tk()
window.title("Top 100 Boardgames")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


new_label = Label(text="Enter ranking to get boardgame and stats", font=("Arial", 12, "bold"))
new_label.grid(column=3, row=0)
new_label.config(padx=20, pady=20)

button = Button(text="Click Here", command=button_clicked)
button.grid(column=3, row=3)

input = Entry(width=50)
input.grid(column=3, row=2)

window.mainloop()
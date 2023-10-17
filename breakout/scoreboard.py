from turtle import Turtle

x = 2

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shapesize(stretch_len=0.1, stretch_wid=0.1)
        self.penup()
        self.goto(0, -350)
        self.pendown()
        self.score = 0
        self.points_needed = 20
        self.color("White")
        self.write(f"Your score is: {self.score}, Try to get to {self.points_needed} ", False, align= "center", font=('Arial', 20, 'normal'))

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.write(f"Your score is:{self.score}", False, align= "center", font=('Arial', 20, 'normal'))

    def next_level(self):
        global x
        self.clear()
        self.write(f"Congrats, you beat the level, in 10 seconds the next level will start. See if you can score {self.points_needed * x}", False, align= "center", font=('Arial', 20, 'normal'))
        self.score = 0
        x += 1
    def lose_game(self):
        self.clear()
        self.write(
            "Congrats loser! you lost again!..restart in 5..4..3..2..1 ",
            False, align="center", font=('Arial', 20, 'normal'))
        self.score = 0

from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=7, stretch_wid=1)
        self.penup()
        self.goto(position)

    def right(self):
        new_x = self.xcor() + 80
        self.goto(new_x, self.ycor())

    def left(self):
        new_x = self.xcor() + -80
        self.goto(new_x, self.ycor())

    def reset_pos(self):
        self.goto(0,-220)



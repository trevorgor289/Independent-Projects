from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Blocks(Turtle):

    def __init__(self):
        super().__init__()

        self.row = []
        self.shape('turtle')
        self.color('green')
        self.shapesize(stretch_len=20, stretch_wid=20)



    def create_block(self, level):
        x = 0
        y = 0


        for n in range(level*2):
            for n in range(15):
                self.penup()
                self.shapesize(stretch_len=0.1, stretch_wid=0.1)
                block = Turtle("square")
                block.left(90)
                block.shapesize(stretch_wid=5, stretch_len=1,)
                block.penup()
                new_x = 710 - x
                new_y = 350 - y
                block.goto(new_x, new_y)
                x += 110
                self.row.append(block)

            y += 30
            x = 0
        block_color = random.choice(COLORS)
        for block in self.row:
            block.color(block_color)











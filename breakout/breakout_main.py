from turtle import Screen, Turtle
from paddle import Paddle
import time
from ball import Ball
from blocks import Blocks
from scoreboard import Scoreboard




screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

game_is_on = True




r_paddle = Paddle((0,-220))




ball = Ball()
blocks = Blocks()
level = 1
blocks.create_block(level)
scoreboard = Scoreboard()
screen.update()

print(len(blocks.row))

screen.onkeypress(r_paddle.right, "Right")
screen.onkeypress(r_paddle.left, "Left")
screen.listen()


x = 0

z = 1

q = 1

s = 0

next_level = 1

time.sleep(1)

while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #hitting the wall

    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    if ball.xcor() > 745 or ball.xcor() < -745:
        ball.bounce_x()


    # hitting right side of paddle

    if ball.distance(r_paddle) < 20 and ball.ycor() < -190 and ball.xcor() > r_paddle.xcor() and ball.x_move < 0 and ball.y_move < 0:
        ball.bounce_y()


    if 20 < ball.distance(r_paddle) < 50 and ball.ycor() < -190 and ball.xcor() > r_paddle.xcor() and ball.x_move < 0 and ball.y_move < 0:
        ball.bounce_y()
        ball.bounce_x()


    if ball.distance(r_paddle) < 50 and ball.ycor() < -190 and ball.xcor() > r_paddle.xcor() and ball.x_move > 0 and ball.y_move < 0:
        ball.bounce_y()

    #hitting left side of paddle

    if ball.distance(r_paddle) < 50 and ball.ycor() < -190 and ball.xcor() < r_paddle.xcor() and ball.x_move < 0 and ball.y_move < 0:
        ball.bounce_y()


    if 20 < ball.distance(r_paddle) < 50 and ball.ycor() < -190 and ball.xcor() < r_paddle.xcor() and ball.x_move > 0:
        ball.bounce_y()
        ball.bounce_x()


    if ball.distance(r_paddle) < 20 and ball.ycor() < -190 and ball.xcor() < r_paddle.xcor() and ball.x_move > 0:
        ball.bounce_y()





    #missing the paddle and losing the game

    if ball.ycor() < -235:
        for square in blocks.row:
            square.ht()
            square.shapesize(stretch_len=0.001, stretch_wid=0.001)
            square.penup()
            square.goto(-500, -500)
        blocks.row.clear()
        scoreboard.lose_game()
        x = 0
        s = 0
        z = 1
        q = 1

        time.sleep(2)
        blocks.create_block(level)
        ball.reset_position()
        r_paddle.reset_pos()
        time.sleep(3)

    #detect collision with block and clear block out


    for square in blocks.row:
        if -30 < (ball.ycor() - square.ycor()) < 30 and -50 < (ball.xcor() - square.xcor()) < 50:
            ball.bounce_y()
            square.ht()
            square.shapesize(stretch_len=0.001, stretch_wid=0.001)
            square.penup()
            square.goto(-500, -500)
            scoreboard.update_scoreboard()
            x += 1
            s += 1

    #detecting hitting edge of block

    for square in blocks.row:
        if ball.ycor() == square.ycor() and -50 < (ball.xcor() - square.xcor()) < 50:
            ball.bounce_x()
            square.ht()
            square.shapesize(stretch_len=0.001, stretch_wid=0.001)
            square.penup()
            square.goto(-500, -500)
            scoreboard.update_scoreboard()
            x += 1
            s += 1

    if x == 10:
        ball.move_speed *= .9
        x = 0
        r_paddle.shapesize(stretch_len=9 - z, stretch_wid=1)
        z += 0.15


    if s == (next_level * 2):


        for square in blocks.row:
            square.ht()
            square.shapesize(stretch_len=0.001, stretch_wid=0.001)
            square.penup()
            square.goto(-500, -500)
        blocks.row.clear()
        next_level = level + q
        scoreboard.next_level()
        blocks.create_block(next_level)

        x = 0
        s = 0
        z = 1
        q += 1
        r_paddle.reset_pos()
        ball.reset_position()
        time.sleep(5)





screen.exitonclick()
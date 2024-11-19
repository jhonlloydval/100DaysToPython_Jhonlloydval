# Making a PING PONG GAME

from turtle import *
from D23_pong import Paddle
from D23_scoreboard import Scoreboard
import time
from D23_ball import Ball

# SCREEN SET-UP
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("My Ping Pong Game")
screen.tracer(0)

# CREATING PADDLES AND BALL
player = Paddle()
player.goto(-370,0)

enemy = Paddle()
enemy.goto(370,0)

ball = Ball()

# CREATING LINE
y_cor = 280
for lines in range(21):
    lines = Paddle()
    lines.create_line()
    y_cor -= 25
    lines.goto(0, y_cor)

# CREATING SCOREBOARD
player_score = Scoreboard((-50, 230))
enemy_score = Scoreboard((50, 230))

# KEY BINDINGS FOR MOVEMENT
screen.listen()
screen.onkey(player.up, "w")
screen.onkey(player.down, "s")
screen.onkey(enemy.up, "Up")
screen.onkey(enemy.down, "Down")

not_game_over = True
while not_game_over:
    time.sleep(0.1)
    screen.update()
    ball.move()
    enemy.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # DETECT COLLISION WITH RIGHT PADDLE
    if ball.distance(enemy) < 50 and ball.xcor() > 340: 
        ball.bounce_x()
    if ball.distance(player) < 50 and ball.xcor() < -330:
        ball.bounce_x()


# UPDATE SCREEN TO RENDER PADDLES
screen.update()

# EXIT ON CLICK
screen.exitonclick()
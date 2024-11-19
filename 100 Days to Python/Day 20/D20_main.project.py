# SNAKE GAME PROJECT

from turtle import Turtle, Screen
import time
from D20_snake import Snake
from D20_food import Food
from D20_scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("My Snake Game")
screen.tracer(0)

# Create a snake body
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")



# Moving snake bwy itself
not_game_over = True

while not_game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect colision with food.

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect colision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        not_game_over = False
        scoreboard.game_over()

    # Detect colision with wall

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            not_game_over = False
            scoreboard.game_over()





screen.exitonclick()
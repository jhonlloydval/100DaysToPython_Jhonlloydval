# MAKING THE BALL GAME
from turtle import *
import random
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.last_bounce_time = 0

    def create_ball(self):
        color_choices = ["white", "spring green", "burlywood", "crimson", "antique white", "gold", "silver", "royal blue", "lavender", "tomato"]
        rand_color = random.choice(color_choices)
        self.shape("circle")
        self.color(rand_color)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        current_time = time.time()
        if current_time - self.last_bounce_time > 0.1:  # Add a 0.1-second cooldown
            self.x_move *= -1
            self.move_speed *= 0.9  # Optional: Speed up slightly with each bounce
            self.last_bounce_time = current_time

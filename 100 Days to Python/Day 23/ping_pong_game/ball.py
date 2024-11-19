from turtle import *
import random

color_choices = ["white", "spring green", "burlywood", "crimson", "antique white", "gold", "silver", "royal blue", "lavender", "tomato"]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def create_ball(self):
        self.shape("circle")
        self.color(random.choice(color_choices))

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
        self.color(random.choice(color_choices))

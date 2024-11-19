from turtle import *

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        
    def create_line(self):
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.1, stretch_len=0.5)
        self.setheading(270)
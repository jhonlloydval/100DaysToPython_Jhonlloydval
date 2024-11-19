# Making the moving something
from turtle import *
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.7, stretch_len=4)
        self.setheading(270)

    def move(self):
        self.forward(20)
        y_loc = self.ycor()
        if y_loc < -250:
            self.setheading(90)
        elif y_loc > 250:
            self.setheading(270)

    def create_line(self):
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.1, stretch_len=0.5)
        self.setheading(270)
        
    def down(self):
        y_loc = self.ycor()
        if y_loc < -270:
            pass
        else:
            self.setheading(270)
            self.forward(30)

    def up(self):
        y_loc = self.ycor()
        if y_loc > 270:
            pass
        else:
            self.setheading(90)
            self.forward(30)
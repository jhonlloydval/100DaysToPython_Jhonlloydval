# SNAKE CLASS\
from turtle import Turtle
from turtle import *

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

starting_positions = [(0,0), (-20, 0), (-40,0)]

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle()
        snake.penup()
        snake.shape("square")
        snake.color("white")
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        self.last_direction = self.head.heading()
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
    
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.last_direction != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.last_direction != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.last_direction != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.last_direction != RIGHT:
            self.head.setheading(LEFT)

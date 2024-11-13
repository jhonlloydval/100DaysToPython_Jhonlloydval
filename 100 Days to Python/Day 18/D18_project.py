# Hirst painting project

# import colorgram
# colors = colorgram.extract('/Users/jhonlloydval/GitHub/100DaysToPython_Jhonlloydval/100 Days to Python/Day 18/image_1.jpg', 6)
# first_color = colors[0]

# def get_rgb(x):
#     get = colors[x].rgb
#     return (get[0], get[1], get[2])

# extracted_colors = []
# for x in range(len(colors)):
#     extracted_colors.append(get_rgb(x))

import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

color_list = [(163, 85, 21), (6, 35, 52), (55, 39, 12), (166, 163, 49), (19, 45, 25)]

turtle1 = Turtle()
turtle1.penup()
turtle1.speed(0)
turtle1.hideturtle()


turtle1.setheading(225)
turtle1.forward(300)
turtle1.setheading(0)

num_of_dots = 0
while num_of_dots < 100:
    for _ in range(10):
        turtle1.dot(20, random.choice(color_list))
        turtle1.forward(50)
        
    turtle1.setheading(90)
    turtle1.forward(50)
    turtle1.setheading(180)
    turtle1.forward(500)
    turtle1.setheading(0)
    num_of_dots += 10



screen.exitonclick()


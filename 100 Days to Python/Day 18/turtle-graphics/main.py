from turtle import Turtle, Screen, pos
import random
import turtle as t

turtle1 = Turtle()
turtle1.shape("turtle")
turtle1.color("PaleTurquoise4")
turtle1.pensize(1)
turtle1.speed(0)
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b


# Turtle Challenge 2
# for steps in range(25):
#     turtle1.forward(3)
#     tp = turtle1.pos()
#     turtle1.teleport(tp[0] + 5, tp[1])


# Turtle Challenge 3
# shape = 3
# while shape != 11:
#     turtle1.color(random_color()))
#     for x in range(shape):
#         turtle1.forward(100)
#         turtle1.right(360/shape)
#     shape += 1


# Turtle Challenge 4
# turtle_rotation = [90, 180, 270, 0]
# for x in range(100):
#     turtle1.color(random_color())
#     turtle1.setheading(random.choice(turtle_rotation))
#     turtle1.forward(30)

# Turtle Challenge 5
direction = 0
while direction <= 360:
    turtle1.color(random_color())
    turtle1.circle(100)
    turtle1.setheading(direction)
    direction += 3

screen = Screen()
screen.exitonclick()

# Turtle game project using OOP

from turtle import *
import random
screen = Screen()
screen.setup(width=500, height=400)

turtle_colors = """
Which turtle will win the race? Enter a color:
- Omri: Tomato
- Mark: Lavender
- Sam: Antique White
- Hubert: Silver
- Micoh: Crimson
- Sean: Gold
- Melvin: Royal Blue
- Lloyd: Spring Green
- Benedick: Burlywood
"""
        
# MAKING THE TURTLES
omri = Turtle()
mark = Turtle()
sam = Turtle()
hubert = Turtle()
micoh = Turtle()
sean = Turtle()
melvin = Turtle()
lloyd = Turtle()
benedick = Turtle()


# SETTING UP THE TURTLES

y_start = -100
y_gap = 25

names = ["Omri", "Mark", "Sam", "Hubert", "Micoh", "Sean", "Melvin", "Lloyd", "Benedick"]
turtles = [omri, mark, sam, hubert, micoh, sean, melvin, lloyd, benedick]
colors = ["tomato", "lavender", "antique white", "silver", "crimson", "gold", "royal blue", "spring green", "burlywood"]

correct_bet = True
while correct_bet:
    user_bet = screen.textinput(title="Make your bet", prompt=turtle_colors).lower()
    if user_bet not in colors:
        print("The color is not in the choices.")
        continue
    else:
        turtle_index = colors.index(user_bet)
        print(f"Your bet is '{user_bet}': {names[turtle_index]}")
        correct_bet = False
        

for index, turtle in enumerate(turtles):
    turtle.shape("turtle")
    turtle.penup()
    turtle.fillcolor(colors[index])
    turtle.goto(-200, y_start + index * y_gap)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.fillcolor()
            winner_name = colors.index(winning_turtle)
            winner = names[winner_name]
            if winning_turtle == user_bet.lower():
                print(f"You've won! The winning turtle is {user_bet} : {winner} .")
            else:
                print(f"You've lost. The winning turtle is {winning_turtle} : {winner}.")
            is_race_on = False
        random_move = random.randint(0,10)
        turtle.forward(random_move)


screen.exitonclick()
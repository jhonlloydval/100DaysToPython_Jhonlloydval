from turtle import *

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score =0 
        self.goto(position)
        self.create_scoreboard()
        self.update_scoreboard()

    def create_scoreboard(self):
        self.color("white")
        self.hideturtle()
        self.penup()

    def update_scoreboard(self):
        self.write(f"{self.score}", align="center", font=("Arial", 50, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, -280)
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_score()

    def game(self):
        self.home()
        self.write(arg=f"Game", align="center", font=FONT)


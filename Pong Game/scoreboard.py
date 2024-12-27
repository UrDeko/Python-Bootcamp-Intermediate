from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(100, 200)
        self.write(arg=f"{self.r_score}", font=("Courier", 80, "normal"))
        self.goto(-120 ,200)
        self.write(arg=f"{self.l_score}", font=("Courier", 80, "normal"))
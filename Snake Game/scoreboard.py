from turtle import Turtle
ALIGN = "center"
FONT = ("Helvetica", 24, "normal")
HIGHEST_SCORE_FILE = "Python Bootcamp/Intermediate/Snake Game/highest_score.txt"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Python Bootcamp/Intermediate/Snake Game/highest_score.txt") as f:
            self.highest_score = int(f.read())
        self.color("lime")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}    Highest score: {self.highest_score}", align=ALIGN, font=FONT)

    def increase(self):
        self.score += 1

        if self.score > self.highest_score:
            self.highest_score = self.score

            with open(HIGHEST_SCORE_FILE, "w") as f:
                f.write(str(self.highest_score))

        self.update_score()

    def game_over(self):
        self.home()
        self.write(arg="GAME", align=ALIGN, font=FONT)


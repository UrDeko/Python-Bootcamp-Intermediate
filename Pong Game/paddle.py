from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=0.5)
        self.color("white")
        self.penup()
        self.goto(coordinates)

    def move_up(self):
        y_pos = self.ycor() + 20
        self.goto(self.xcor(), y_pos)

    def move_down(self):
        y_pos = self.ycor() - 20
        self.goto(self.xcor(), y_pos)

    
from turtle import Turtle

FONT = ("Courier", 12, "normal")
ALIGN = "center"
COLOR = "blue"
SHAPE = "circle"

class State(Turtle):

    def __init__(self, name, coordinates):
        super().__init__()
        self.name = name
        self.hideturtle()
        self.color(COLOR)
        self.shape(SHAPE)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1)
        self.penup()
        self.goto(coordinates)
        self.showturtle()
        self.write(self.name, align=ALIGN, font=FONT)
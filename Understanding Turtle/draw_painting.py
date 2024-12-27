import random

from turtle import Turtle, Screen

COLORS = ("green", "purple", "blue", "red", "orange", "yellow", "lime", "pink")

def set_pos(x, y, t_object):
    t_object.penup()
    t_object.setpos(x, y)
    t_object.pendown()

def get_rgb_value():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

def draw_painting():
    screen = Screen()
    screen.colormode(255)

    timmy = Turtle()
    timmy.hideturtle()
    timmy.shape("circle")
    timmy.speed("fastest")

    set_pos(-320, -250, timmy)
    entry_point = timmy.pos()

    for i in range(10):
        set_pos(entry_point[0], entry_point[1] + i * 40, timmy)

        for _ in range(10):
            color = get_rgb_value()
            # timmy.dot(20, random.choice(COLORS))
            timmy.dot(20, color)
            timmy.penup()
            timmy.forward(40)
            timmy.pendown()

    screen.exitonclick()

if __name__ == "__main__":
    draw_painting()
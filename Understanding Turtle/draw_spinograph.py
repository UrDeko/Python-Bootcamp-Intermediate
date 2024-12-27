import random

from turtle import Turtle, Screen

GAP_SIZE = 10
SPEED = "fastest"

def get_rgb_value():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

def draw_spinograph(size_of_gap, t_object):
    for _ in range(int(360 / size_of_gap)):
        color = get_rgb_value()
        t_object.pencolor(color)
        t_object.circle(100)
        # heading = t_object.heading()
        # t_object.setheading(heading + size_of_gap)
        t_object.left(size_of_gap)

if __name__ == "__main__":
    screen = Screen()
    screen.colormode(255)

    timmy = Turtle()
    timmy.speed(SPEED)

    draw_spinograph(GAP_SIZE, timmy)

    screen.exitonclick()
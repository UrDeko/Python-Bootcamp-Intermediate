import random

from turtle import Turtle, Screen

SPEED = "fastest"
WIDTH = 10
COLORS = ("green", "purple", "blue", "red", "orange", "yellow", "lime", "pink")
DIRECTIONS = (0, 90, 180, 270)
STEPS = 400


# Ex. 4
def get_rgb_value():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

def generate_random_walk(t_object):
    t_object.hideturtle()
    t_object.width(WIDTH)
    t_object.speed(SPEED)


    for _ in range(STEPS):
        color = get_rgb_value()
        t_object.pencolor(color)
        t_object.setheading(random.choice(DIRECTIONS))
        t_object.forward(20)

# Ex. 3
def draw_shapes(t_object):
    for i in range(3, 11):
        t_object.pencolor(COLORS[i-3])
        angle = 360 / i

        for j in range(i):
            t_object.forward(100)
            t_object.right(angle)

# Ex. 2
def draw_dashed_line(t_object):
    for i in range(24):
        if i % 2 == 0:
            t_object.pendown()
        else:
            t_object.penup()
        t_object.forward(10)

    t_object.pendown()
    for _ in range(8):
        t_object.right(45)
        t_object.forward(100)

# Ex. 1
def move_turtle(t_object):
    t_object.hideturtle()
    t_object.penup()
    t_object.back(50)
    t_object.right(90)
    t_object.forward(120)
    t_object.right(90)
    t_object.forward(120)
    t_object.right(270)
    t_object.pendown()
    t_object.circle(120)
    t_object.penup()
    t_object.left(90)
    t_object.forward(60)
    t_object.right(90)
    t_object.pendown()
    t_object.circle(60)
    t_object.circle(60)
    t_object.circle(60)


if __name__ == "__main__":
    screen = Screen()
    screen.colormode(255)
    timmy = Turtle()

    # move_turtle(timmy)
    # draw_dashed_line(timmy)
    # draw_shapes(timmy)
    generate_random_walk(timmy)

    screen.exitonclick()
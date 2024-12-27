from turtle import Turtle, Screen
import random

is_game_on = False

window = Screen()
window.setup(width=500, height=400)

user_pick = window.textinput(title="Turtle Race", prompt="Choose your winner")
colours = ["blue", "green", "yellow", "orange", "red"]
all_turtles = []
y_start = -60

for colour in colours:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colour)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_start)
    y_start += 40
    all_turtles.append(new_turtle)

is_game_on = True

while is_game_on:

    for racer in all_turtles:

        if racer.xcor() > 230:
            winner = racer.fillcolor()
            is_game_on = False

            if user_pick == winner:
                print(f"You win! The {winner} turtle was first")
            else:
                print(f"It's OK, the {winner} turtle won")

            break

        pace = random.randint(0, 10)
        racer.forward(pace)


window.exitonclick()
from turtle import Turtle, Screen

timmy = Turtle()
timmy.color("orange")
timmy.shape("turtle")

for _ in range(4):
    timmy.right(90)
    timmy.forward(100)

window = Screen()
window.exitonclick()
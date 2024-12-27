import time

from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 600

window = Screen()
window.setup(width=WIDTH, height=HEIGHT)
window.title("Pong")
window.bgcolor("black")
window.tracer(0)
window.listen()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
pong_ball = Ball()
score = Scoreboard()

window.onkey(r_paddle.move_up, "Up")
window.onkey(r_paddle.move_down, "Down")

window.onkey(l_paddle.move_up, "w")
window.onkey(l_paddle.move_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(pong_ball.pace)
    window.update()
    pong_ball.move()
    
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -270:
        pong_ball.bounce_y()

    if pong_ball.distance(r_paddle) < 50 and pong_ball.xcor() > 330 or \
       pong_ball.distance(l_paddle) < 50 and pong_ball.xcor() < -330:
        pong_ball.bounce_x()
        pong_ball.pace *= 0.9

    if pong_ball.xcor() > 380:
        score.l_score += 1
        score.update()
        pong_ball.reset()

    if pong_ball.xcor() < -380:
        score.r_score += 1
        score.update()
        pong_ball.reset()

window.exitonclick()
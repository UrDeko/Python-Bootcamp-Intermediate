import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

window = Screen()
window.setup(width=600, height=600)
window.bgcolor("cornflower blue")
window.title("Snake Game")
window.tracer(0)
borders = window.textinput("Game mode", "Borders: ON/OFF").lower()

score = Scoreboard()
snake = Snake()
apple = Food()

window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.right, "Right")
window.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    window.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(apple) < 15:
        score.increase()
        new_segment = snake.segments[-1].clone()
        snake.segments.append(new_segment)
        apple.update_position()

    if borders == "on":
        if snake.head.xcor() > 280 or snake.head.xcor() < -300 or \
           snake.head.ycor() > 300 or snake.head.ycor() < -280:
            score.game_over()
            game_is_on = False
    else:
        if snake.head.xcor() > 280:
            y_cor = snake.head.ycor()
            snake.head.goto(-280, y_cor)
        elif snake.head.xcor() < -300:
            y_cor = snake.head.ycor()
            snake.head.goto(280, y_cor)
        elif snake.head.ycor() > 300:
            x_cor = snake.head.xcor()
            snake.head.goto(x_cor, -280)
        elif snake.head.ycor() < -280:
            x_cor = snake.head.xcor()
            snake.head.goto(x_cor, 280)

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False

window.exitonclick()
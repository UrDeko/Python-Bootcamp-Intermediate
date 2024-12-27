import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.all_cars = []
        self.pace = STARTING_MOVE_DISTANCE

    def create_car(self):
        a = random.randint(1, 6)

        if a == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            y_start = random.randint(-240, 240)
            car.goto(300, y_start)
            car.setheading(180)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.pace)

    def speed_up(self):
        self.pace += MOVE_INCREMENT

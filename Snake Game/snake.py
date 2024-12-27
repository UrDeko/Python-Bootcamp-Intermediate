from turtle import Turtle

START_POSITIONS = [(0, 0),(-20, 0),(-40, 0)]
MOVE_STEP = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake():

    def __init__(self):
        self.segments = []
        self._create_snake()
        self.head = self.segments[0]

    def _create_snake(self):
        for coordinates in START_POSITIONS:
            segment = Turtle(shape="square")
            segment.color("lime","coral")
            segment.penup()
            segment.goto(coordinates)
            self.segments.append(segment)

    def move(self):
        nr_segments = len(self.segments)

        for i in range(nr_segments - 1, 0, -1):
            new_position = self.segments[i - 1].position()
            self.segments[i].goto(new_position)

        self.segments[0].forward(MOVE_STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

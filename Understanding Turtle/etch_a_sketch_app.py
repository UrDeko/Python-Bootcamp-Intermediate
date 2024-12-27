from turtle import Turtle, Screen

class EtchASketch():

    def __init__(self):
        self.tim = Turtle()
        self.window = Screen()

    def _move_forwards(self):
        self.tim.forward(10)

    def _move_backwards(self):
        self.tim.backward(10)

    def _move_clockwise(self):
        self.tim.left(10)

    def _move_counter_clockwise(self):
        self.tim.right(10)

    def _clean_window(self):
        self.tim.clear()
        self.tim.penup()
        self.tim.home()
        self.tim.pendown()

    def play(self):
        self.window.listen()
        self.window.onkey(key="w", fun=self._move_forwards)
        self.window.onkey(key="s", fun=self._move_backwards)
        self.window.onkey(key="a", fun=self._move_clockwise)
        self.window.onkey(key="d", fun=self._move_counter_clockwise)
        self.window.onkey(key="c", fun=self._clean_window)

        self.window.exitonclick()


if __name__ == "__main__":
    game = EtchASketch()
    game.play()
from turtle import Turtle, Screen


class Events:
    def __init__(self):
        self.timmy = Turtle()
        self.screen = Screen()

    def move_forward(self):
        self.timmy.forward(10)

    def move_backwards(self):
        self.timmy.backward(10)

    def turn_clockwise(self):
        self.timmy.right(5)

    def turn_anti_clock_wise(self):
        self.timmy.left(5)

    def clear_screen(self):
        self.screen.resetscreen()


from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.turtlesize(stretch_len=5)
        self.penup()
        self.goto(x_pos, y_pos)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.backward(20)

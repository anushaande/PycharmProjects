from turtle import Turtle

STARTING_POSITION = (0.00, -330.00)


class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_forward(self):
        self.forward(10)

    def go_right(self):
        new_x = self.xcor() + 10
        new_y = self.ycor()
        self.goto(new_x, new_y)

    def go_left(self):
        new_x = self.xcor() - 10
        new_y = self.ycor()
        self.goto(new_x, new_y)

    def reset(self):
        self.goto(STARTING_POSITION)

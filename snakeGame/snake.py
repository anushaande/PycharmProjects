from turtle import Turtle

STEPS = 20  # Declaring a constant
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]
        self.tail = self.squares[-1]

    def create_snake(self):  # Creating the snake
        xcor = 0.00
        ycor = 0.00
        for i in range(3):
            square = Turtle("square")
            square.penup()
            square.color("white")
            square.setposition(xcor, ycor)
            xcor -= 20
            self.squares.append(square)

    def move(self):  # Moving the snake
        goto_pos = self.head.pos()
        self.head.forward(STEPS)
        for i in range(1, len(self.squares)):
            next_pos = self.squares[i].position()
            self.squares[i].goto(goto_pos)
            goto_pos = next_pos

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(0)

    def grow(self):
        if self.head.heading() == UP:
            new_xcor = self.tail.xcor()
            new_ycor = self.tail.ycor() - 20
        if self.head.heading() == DOWN:
            new_xcor = self.tail.xcor()
            new_ycor = self.tail.ycor() + 20
        if self.head.heading() == RIGHT:
            new_xcor = self.tail.xcor() - 20
            new_ycor = self.tail.ycor()
        if self.head.heading() == LEFT:
            new_xcor = self.tail.xcor() + 20
            new_ycor = self.tail.ycor()
        square = Turtle("square")
        square.penup()
        square.color("white")
        square.setposition(new_xcor, new_ycor)
        self.squares.append(square)

    def collide_with_wall(self):
        if self.head.xcor() > 285 or self.head.xcor() < -285 or self.head.ycor() > 285 or self.head.ycor() < -285:
            return True

    def collide_with_itself(self):
        for square in self.squares[1:]:
            if self.head.distance(square) < 15:
                return True

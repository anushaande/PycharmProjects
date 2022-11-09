from turtle import Turtle
import random


class CreateTurtle:
    def __init__(self, color, x, y):
        self.turtle = Turtle()
        self.turtle.color(color)
        self.turtle.shape("turtle")
        self.turtle.pos(x, y)


class TurtleList:
    def __init__(self):
        turtles = []
        colors = ["red", "blue", "green", "orange", "pink", "purple", "gray", "Yellow"]
        x = -750
        y = 350
        for i in range(7):
            turtle = CreateTurtle(random.choice(colors), x, y)
            turtles.append(turtle)
            y = 350 - 100

    def turtles_in_race(self):
        turtles = []
        for turtle in self.turtles:
            turtles.append(self.turtles[turtle])
        return turtles

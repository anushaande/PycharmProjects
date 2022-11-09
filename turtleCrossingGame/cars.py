from turtle import Turtle
import random

COLORS = ["red", "yellow", "blue", "yellow", "orange", "purple", "pink", "blue", "violet", "indigo"]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.goto(random.randint(380, 400), random.randint(-280, 280))


class Cars:

    def __init__(self):
        self.cars = []
        self.speed = 5
        self.no_of_cars = 1

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            for i in range(self.no_of_cars):
                car = Car()
                self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)

    def level_up(self):
        self.no_of_cars += 1
        self.speed += 2








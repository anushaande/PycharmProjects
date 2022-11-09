import random
import turtle
from turtle import Turtle
import colorgram

turtle.colormode(255)


class TurtleDrawings:
    def __init__(self):
        self.turtle = Turtle()

    def shapes(self, start_with_sides):
        """ This method will take start_with_sides as an input to start drawing a shape with. From there it will draw
         till 10 sides"""
        while start_with_sides < 11:
            self.turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            angle = int(360 / start_with_sides)
            for i in range(start_with_sides):
                self.turtle.forward(100)
                self.turtle.right(angle)
            start_with_sides += 1

    def dotted_line(self, length):
        for i in range(length):
            self.turtle.forward(10)
            self.turtle.color("white")
            self.turtle.forward(10)
            self.turtle.color("black")

    def random_walks(self, moves_count):
        self.turtle.speed(10)
        self.turtle.pensize(10)
        directions = [0, 90, 180, 270]
        for i in range(moves_count):
            self.turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.turtle.forward(30)
            self.turtle.setheading(random.choice(directions))

    def spirograph(self, no_of_circles):
        self.turtle.speed(100)
        for i in range(no_of_circles):
            self.turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            angle = 360 / no_of_circles
            self.turtle.circle(100)
            self.turtle.left(angle)

    def extract_rgb_colors(self, image):
        colors = colorgram.extract(image, 30)
        color_pallet = []
        for color in colors:
            tup = (color.rgb.r, color.rgb.g, color.rgb.b)
            color_pallet.append(tup)
        return color_pallet

    def hist_painting(self):
        color_pallet = self.extract_rgb_colors("spot_painting.jpg")
        print(color_pallet)
        x = -200.00
        y = -200.00
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.setpos(x, y)
        for i in range(10):
            for j in range(9):
                self.turtle.dot(20, random.choice(color_pallet))
                self.turtle.forward(50)
            self.turtle.dot(20, random.choice(color_pallet))
            y += 50.00
            self.turtle.setpos(x, y)

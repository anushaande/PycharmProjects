from turtle import Turtle, Screen
from turtle_drawings import TurtleDrawings
from random import random


shape = int(input("Please enter your choice 1.shapes 2.dotted_line 3.random_walks 4.spirograph 5.hist_paining."
                  " 1 or 2 or 3 or 4 or 5?"))

draw = TurtleDrawings()

if shape == 1:
    draw.shapes(3)
elif shape == 2:
    draw.dotted_line(15)
elif shape == 3:
    draw.random_walks(200)
elif shape == 4:
    draw.spirograph(100)
elif shape == 5:
    draw.hist_painting()

my_screen = Screen()
my_screen.exitonclick()
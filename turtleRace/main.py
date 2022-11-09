from turtle import Turtle, Screen
# from race import CreateTurtle, TurtleList
import random

screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="red, green, blue, orange"
                                                          ", pink, purple, gray, yellow.Which turtle will win your race? Enter a color: ")
all_turtles = []

colors = ["red", "blue", "green", "orange", "pink", "purple", "gray", "Yellow"]
pos_x = -235
pos_y = 180

for i in range(0, len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.setposition(x=pos_x, y=pos_y)
    pos_y -= 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == turtle.pencolor:
                print(f"Your {winning_color} turtle won! Congratulations!!!!!!!!!")
            else:
                print(f"The winner is {winning_color}. You chose {user_bet}. Sorry! Better luck next time!")
            is_race_on = False

screen.exitonclick()
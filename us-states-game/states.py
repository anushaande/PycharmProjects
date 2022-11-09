from turtle import Turtle


def write_state(xcor, ycor, state):
    turtle = Turtle()
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(xcor, ycor)
    turtle.write(state)


def game_over():
    turtle = Turtle()
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0.00, 0.00)
    turtle.write("Congratulations! You Guessed all the 50 States", align="center", font=("ariel", 20, "bold"))

def quit_game():
    turtle = Turtle()
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0.00, 0.00)
    turtle.write("You did Great. Find the missing states in missed_states.csv file", align="center", font=("ariel", 15, "bold"))

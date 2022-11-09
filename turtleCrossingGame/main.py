from turtle import Screen
from cars import Cars
from timmy import Timmy
from scoreboard import Scoreboard
import time

screen = Screen()  # Creating the screen
screen.setup(width=800, height=700)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()

tim = Timmy()  # Creating the turtle
screen.onkeypress(fun=tim.go_forward, key="Up")
screen.onkeypress(fun=tim.go_right, key="Right")
screen.onkeypress(fun=tim.go_left, key="Left")
game_is_on = True

cars = Cars()  # Creating Cars
scoreboard = Scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()
    for car in cars.cars:
        if car.distance(tim) < 20:
            game_is_on = False
            scoreboard.game_over()
    if tim.ycor() > 340:
        # print("Timmy won the race!")
        tim.reset()
        cars.level_up()
        scoreboard.update_scoreboard()

screen.exitonclick()

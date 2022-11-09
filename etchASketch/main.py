import turtle

from events import Events
from turtle import Screen

screen = Screen()
event = Events()

screen.listen()
turtle.onkeypress(fun=event.move_forward, key="w")
turtle.onkeypress(fun=event.move_backwards, key="s")
turtle.onkeypress(fun=event.turn_clockwise, key="a")
turtle.onkeypress(fun=event.turn_anti_clock_wise, key="d")
turtle.onkeypress(fun=event.clear_screen, key="c")

screen.exitonclick()

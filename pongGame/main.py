from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time

screen = Screen()  # setting up the black screen

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)  # Tracer method is used to control the animation on screen. when we use 0 the animation is off.

r_paddle = Paddle(x_pos=350, y_pos=0)
l_paddle = Paddle(x_pos=-350, y_pos=0)

ball = Ball()
scoreboard = ScoreBoard()
screen.listen()

screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")

screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:  # r_paddle gets the ball
        scoreboard.r_point()
        ball.bounce_x()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:   # l_paddle gets the ball.
        scoreboard.l_point()
        ball.bounce_x()
    elif ball.xcor() > 380:  # r_paddle lost the ball
        scoreboard.l_point()
        scoreboard.r_lost_point()
        ball.reset()
    elif ball.xcor() < -380:   # l-Paddle lost the ball
        scoreboard.r_point()
        scoreboard.l_lost_point()
        ball.reset()
screen.exitonclick()

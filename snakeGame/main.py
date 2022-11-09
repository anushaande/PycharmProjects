from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

DELAY = 0.1


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

food = Food()
score_board = ScoreBoard()

my_snake = Snake()
# creating an object for Snake class will call create_snake function and creates the snake.
screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")

game_is_on = True
score = 0
while game_is_on:
    screen.update()
    time.sleep(DELAY)
    my_snake.move()
    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.grow()
        score_board.update_score()
    if my_snake.collide_with_wall() or my_snake.collide_with_itself():
        game_is_on = False
        score_board.game_over()
        score_board.update_highest_score()

screen.exitonclick()

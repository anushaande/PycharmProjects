from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-387, 320)
        self.level = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT, align="left")

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER! ", font=FONT, align="center")

from turtle import Turtle

ALIGNMENT = "center"
STYLE = ("Arial", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.color("white")
        self.pencolor("white")
        self.write(arg="Score: 0", align=ALIGNMENT, font=STYLE)

    def update_score(self):
        self.score += 1
        arg = "Score: " + str(self.score)
        self.clear()
        self.write(arg=arg, align=ALIGNMENT, font=STYLE)

    def game_over(self):
        self.goto(0.00, 0.00)
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=STYLE)

    def update_highest_score(self):
        with open("high_score.txt") as high_score:
            highest_score = high_score.read()
        if self.score > int(highest_score):
            with open("high_score.txt", mode="w") as high_score:
                high_score.write(str(self.score))
            self.goto(0.00, -30.00)
            self.write(arg="High Score!", align=ALIGNMENT, font=STYLE)


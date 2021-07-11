from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, -100)

    def lose(self):
        self.write("Game Over", align="center", font=("Courier", 50, "normal"))

    def win(self):
        self.write("Victory!", align="center", font=("Courier", 50, "normal"))

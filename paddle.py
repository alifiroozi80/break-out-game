from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=13)
        self.penup()
        self.goto(x=0, y=-220)

    def right_move(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def left_move(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=900, height=500)
screen.title("break-Out")
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
score = Score()

screen.listen()
screen.onkey(paddle.right_move, "Right")
screen.onkey(paddle.left_move, "Left")

boxes = []
for i in range(-390, 391, 60):
    for j in range(80, 211, 60):
        box = Turtle()
        box.goto(x=i, y=j)
        box.shape("square")
        box.color("white")
        boxes.append(box)

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    if ball.ycor() > 230:
        ball.bounce_y()

    if ball.xcor() > 440 or ball.xcor() < -440:
        ball.bounce_x()

    if ball.distance(paddle) < 130 and ball.ycor() < -200:
        ball.bounce_y()

    if ball.ycor() < -240:
        score.lose()
        break

    for a in boxes:
        if a.distance(ball) < 20:
            ball.bounce_x()
            a.hideturtle()
            boxes.remove(a)

        if len(boxes) == 0:
            score.win()
            break

screen.exitonclick()

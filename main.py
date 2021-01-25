from paddle import Paddle
from turtle import Screen

WIDTH = 600
HEIGHT = 800

screen = Screen()
screen.title( "Pink Pong" )
screen.screensize( WIDTH, HEIGHT )
screen.bgcolor("black")
paddle = Paddle()


def move_up():
    new_y = paddle.ycor() - 20
    paddle.goto( (paddle.xcor(), new_y) )


screen.listen()
screen.onkey(move_up, "Up")

screen.exitonclick()

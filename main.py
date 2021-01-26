# from paddle import Paddle
from turtle import Screen, Turtle

WIDTH = 600
HEIGHT = 800
position = (450, 0)
screen = Screen()
screen.title("Pink Pong")
screen.screensize(WIDTH, HEIGHT)
screen.bgcolor("black")

square = Turtle("square")
square.penup()
square.color("white")
square.shapesize(stretch_len=1, stretch_wid=5)
square.speed("fastest")
square.setposition(position)


def move_up():
    new_y = square.ycor() + 20
    square.goto((square.xcor(), new_y))


def move_down():
    new_y = square.ycor() - 20
    square.goto((square.xcor(), new_y))


screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

screen.exitonclick()

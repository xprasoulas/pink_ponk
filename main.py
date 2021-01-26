from turtle import Screen
from paddle import Paddle
WIDTH = 600
HEIGHT = 800

screen = Screen()
screen.title("Pink Pong")
screen.screensize(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.tracer()
r_paddle = Paddle(x_position=(400, 0))
l_paddle = Paddle(x_position=(-400, 0))

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()

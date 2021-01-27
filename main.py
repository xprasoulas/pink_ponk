from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
WIDTH = 600
HEIGHT = 800
scoreboard = Scoreboard()
screen = Screen()
screen.title("Pink Pong")
screen.screensize(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.tracer()
r_paddle = Paddle(x_position=(400, 0))
l_paddle = Paddle(x_position=(-400, 0))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move_it()
    # collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score()


    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_score()

screen.exitonclick()

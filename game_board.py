from turtle import Screen

WIDTH = 600
HEIGHT = 800


class GameBoard:
    def __init__(self):
        self.new_screen()

    def new_screen(self):
        screen = Screen()
        screen.title("Pink Pong")
        screen.screensize(WIDTH, HEIGHT)
        screen.bgcolor("black")
        screen.exitonclick()

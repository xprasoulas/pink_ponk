from turtle import Turtle


class Paddle:
    def __init__(self):
        self.width = 20
        self.height = 100
        self.position = (0, 0)
        self.create_paddle()

    def create_paddle(self):
        stack = []
        for _ in range(3):
            square2 = Turtle("square")
            square2.penup()
            square2.color("white")
            stack.append(square2)

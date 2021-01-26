from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.speed(1)


    def move_it(self):
        self.setheading(45)
        self.forward(500)


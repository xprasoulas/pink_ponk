from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.width = 20
        self.height = 100
        self.position = (360, 0)
        self.create_paddle()

    def create_paddle(self):
        square = Turtle("square")
        square.penup()
        square.color("white")
        square.shapesize(stretch_len=1, stretch_wid=3)
        square.speed("fastest")
        square.setposition(self.position)


    def move_up(self):
        new_y = self.ycor() - 20
        self.goto((self.xcor(), new_y))


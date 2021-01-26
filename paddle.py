from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.position = x_position
        self.create_paddle(self.position)

    def create_paddle(self, place):
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.speed("fastest")
        self.setposition(place)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto((self.xcor(), new_y))

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto((self.xcor(), new_y))

from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.speed(1)
        self.x_move = 10
        self.y_move = 10

    def move_it(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        # Collision with top
        if self.ycor() > 300 or self.ycor() < -300:
            self.bounce_y()



    # Change the angle when collision is made with walls
    def bounce_y(self):
        self.y_move *= -1

    # Change when collision is made with paddle
    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()



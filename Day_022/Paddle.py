from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, tuple):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1, 5)
        self.setheading(90)
        self.goto(tuple)

    def up(self):
        self.fd(20)

    def down(self):
        self.back(20)

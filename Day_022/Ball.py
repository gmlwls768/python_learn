from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.A = 10
        self.B = 10
        self.speed = 0.1

    def move(self):
        new_x = self.xcor() + self.A
        new_y = self.ycor() + self.B
        self.goto(new_x, new_y)

    def bounce(self):
        self.B *= -1

    def change(self):
        self.A *= -1
        self.speed *= 0.9

    def resetposition(self):
        self.speed = 0.1
        self.goto(0, 0)
        self.A *= -1

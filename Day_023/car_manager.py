from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.setheading(180)
        self.penup()
        sel_color = random.choice(COLORS)
        self.color(sel_color)
        ran_car = random.randint(-250, 250)
        self.setposition(300, ran_car)

    def car_move(self):
        self.fd(STARTING_MOVE_DISTANCE)

    def car_speedup(self):
        global STARTING_MOVE_DISTANCE  # if would not to use global separate init func
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

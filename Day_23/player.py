from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setposition(STARTING_POSITION)
        self.setheading(90)

    def player_move(self):
        self.fd(MOVE_DISTANCE)

    def player_finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.setposition(STARTING_POSITION)
            return True

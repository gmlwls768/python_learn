from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFt = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakebody = []
        self.create_snake()
        self.head = self.snakebody[0]

    def make_body(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.xcor
        snake.goto(position)
        self.snakebody.append(snake)

    def create_snake(self):
        self.make_body((0, 0))
        for start_body in range(2):
            self.make_body((self.snakebody[-1].xcor() - MOVE_DISTANCE, 0))

    def extend(self):
        self.make_body(self.snakebody[-1].position())

    def move(self):
        for seg in range(len(self.snakebody) - 1, 0, -1):
            new_x = self.snakebody[seg - 1].xcor()
            new_y = self.snakebody[seg - 1].ycor()
            self.snakebody[seg].goto(new_x, new_y)
        self.snakebody[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFt)

    def right(self):
        if self.head.heading() != LEFt:
            self.head.setheading(RIGHT)

    def reset(self):
        for snake in self.snakebody:
            snake.goto(1000, 1000)
        self.snakebody.clear()
        self.create_snake()
        self.head = self.snakebody[0]

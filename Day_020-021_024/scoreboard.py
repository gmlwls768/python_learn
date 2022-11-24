from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0, 270)
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align=ALIGN,
                   font=FONT)

    def eat(self):
        self.score += 1
        self.clear()
        self.update()

    def over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

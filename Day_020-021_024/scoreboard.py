from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        with open("Day_020-021_024/data.txt") as openfile:
            self.highscore = int(openfile.read())
        self.score = 0
        self.color("white")
        self.goto(0, 270)
        self.update()

    def update(self):
        self.write(f"Score: {self.score} High score: {self.highscore}", align=ALIGN,
                   font=FONT)

    def eat(self):
        self.score += 1
        self.clear()
        self.update()

    # def over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)

    def reset(self):
        if self.highscore < self.score:
            with open("Day_020-021_024/data.txt", "w") as writefile:
                writefile.write(str(self.score))
            self.highscore = self.score

        self.score = 0
        self.clear()
        self.update()

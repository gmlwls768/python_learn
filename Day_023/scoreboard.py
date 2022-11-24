from turtle import Turtle
FONT = ("Courier", 24, "normal")
LEVEL = 1


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(-230, 260)
        self.level = LEVEL
        self.level_up()

    def level_up(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "center", FONT)
        self.level += 1

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", False, "center", FONT)

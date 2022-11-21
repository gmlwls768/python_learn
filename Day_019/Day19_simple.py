from turtle import Turtle, Screen
import random
screen = Screen()
is_race_on = False
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtle_list = []
for i in range(6):
    str = colors[i] + "_turtle"
    str = Turtle(shape="turtle")
    str.color(colors[i])
    str.penup()
    numset = 100
    str.goto(x=-230, y=numset - (i * 30))
    all_turtle_list.append(str)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle_list:
        if turtle.xcor() > 230:
            if user_bet == turtle.fillcolor():
                print("You win")
            else:
                print("You lose")
            print(f"{turtle.fillcolor()} turtle is winner ")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)


tim = Turtle(shape="turtle")


def move_fd():
    tim.fd(10)


def move_bk():
    tim.bk(10)


def move_rt():
    tim.rt(10)


def move_lt():
    tim.lt(10)


def clear():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=move_fd)
screen.onkey(key="s", fun=move_bk)
screen.onkey(key="a", fun=move_lt)
screen.onkey(key="d", fun=move_rt)
screen.onkey(key="c", fun=clear)
# use parameter to func == higher order func
# in higher order func use keyword recommended


screen.exitonclick()

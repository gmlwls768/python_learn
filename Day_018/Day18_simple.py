import colorgram
from turtle import Turtle, Screen, colormode
import random
# import turtle
# tim = turtle.Turtle()
# import turtle as t
# is is alias module
tim = Turtle()
tim.shape("turtle")
tim.color("green")
colormode(255)


def square():
    for i in range(4):
        tim.fd(100)
        tim.right(90)


def line():
    for i in range(15):
        tim.fd(10)
        tim.penup()
        tim.fd(10)
        tim.pendown()


colors = ["DimGray", "Blue", "Teal", "Lime", "Gold",
          "Crimson", "Purple", "DarkSlateBlue"]

color_list = [(239, 239, 238), (233, 237, 233), (235, 236, 240), (242, 234, 237), (43, 105, 171), (233, 206, 116), (225, 152, 87), (183, 50, 77), (118, 87, 50), (228, 120, 147), (214, 61, 80), (109, 110, 188), (130, 175, 210), (115, 185, 139),
              (55, 176, 110), (116, 168, 37), (202, 18, 42), (33, 56, 113), (221, 61, 50), (26, 142, 108), (154, 222, 193), (181, 170, 221), (30, 163, 170), (84, 35, 39), (40, 46, 80), (233, 167, 180), (237, 172, 162), (76, 40, 39), (154, 208, 221), (115, 46, 43)]


def crazy_turtle():
    def loop(num):
        angle = 360/num
        for run in range(num):
            tim.fd(100)
            tim.right(angle)
    for loop_loop in range(3, 11):
        tim.color(random.choice(colors))
        loop(loop_loop)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def walk_turtle():
    tim.pensize(15)
    for i in range(200):
        head = random.randrange(90, 270, 90)
        tim.speed(0)
        tim.right(head)
        # for i in range(3):
        #     hello_color.append(random.randint(1, 255))
        # tim.color((hello_color[0], hello_color[1], hello_color[2]))
        tim.color(random_color())
        tim.fd(random.randint(30, 50))


def circle(gap):
    for i in range(int(360/gap)):
        tim.speed(0)
        tim.color(random_color())
        tim.circle(150)
        tim.setheading(tim.heading() + gap)


def art():
    tim.penup()
    tim.hideturtle()
    tim.setheading(225)
    tim.forward(250)
    tim.setheading(0)
    number_of_dots = 100
    for dot_count in range(1, number_of_dots + 1):
        tim.dot(20, random.choice(color_list))
        tim.speed(0)
        tim.forward(50)

        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)


square()
tim.home()
line()
tim.home()
crazy_turtle()
tim.home()
walk_turtle()
tim.home()
circle(5)
tim.home()
art()
# hello_color_world = []
# colors = colorgram.extract(
#     "../image.webp", 30)
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     hello_color_world.append(new_color)
# print(hello_color_world)


screen = Screen()
screen.exitonclick()

import time
from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from scoreboard import Scoreboard
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")


game_is_on = True


while game_is_on:

    time.sleep(ball.speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320 or ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.change()

    if ball.xcor() > 380:
        ball.resetposition()
        scoreboard.l_get()
    if ball.xcor() < -380:
        ball.resetposition()
        scoreboard.r_get()


screen.exitonclick()

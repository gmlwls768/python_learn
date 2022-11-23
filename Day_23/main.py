import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(fun=player.player_move, key="Up")

game_is_on = True
car_array = []

loop_count = 1

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if loop_count % 6 == 0:
        car = CarManager()

        car_array.append(car)

    for car in car_array:
        car.car_move()
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
        if car.xcor() < -350:
            car_array.remove(car)

    if player.player_finish():
        car.car_speedup()
        scoreboard.level_up()
    loop_count += 1

screen.exitonclick()

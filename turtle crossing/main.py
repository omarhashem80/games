from time import sleep
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()
    car_manager.update()
    for car in car_manager.cars:
        if player.distance(car) < 25:
            game_is_on = False
    if player.update():
        scoreboard.increment_level()
        car_manager.speed_up()

scoreboard.game_over()
screen.exitonclick()

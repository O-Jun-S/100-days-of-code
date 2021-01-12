import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
scoreboard.write_level()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(0, 4) == 0:
        car_manager.make_car()
    car_manager.move_all_cars()

    # Detect player goals.
    if player.is_finish():
        scoreboard.increase_level()
        car_manager.increase_speed()
        car_manager.reset_all_cars()
        player.reset_position()

    # Detect collision with car.
    for car in car_manager.cars:
        if player.distance(car) <= 20:
            scoreboard.write_game_over()
            game_is_on = False
screen.exitonclick()

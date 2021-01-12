from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_GENERATE_X = 300
CAR_GENERATE_Y_MIN = -260
CAR_GENERATE_Y_MAX = 260

CAR_EDGE = -300


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_move = STARTING_MOVE_DISTANCE

    def make_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_len=2)
        new_car.penup()
        new_car.left(180)
        x = CAR_GENERATE_X
        y = random.randint(CAR_GENERATE_Y_MIN, CAR_GENERATE_Y_MAX + 1)
        new_car.goto(x, y)
        self.cars.append(new_car)

    def move_all_cars(self):
        for car in self.cars:
            car.forward(self.car_move)

    def increase_speed(self):
        self.car_move += MOVE_INCREMENT

    def reset_all_cars(self):
        for car in self.cars:
            car.hideturtle()
        self.cars = []

from turtle import Turtle
import random

tom = Turtle()
tom.speed(0)
tom.pensize(15)
colours = ["DarkOrchid", "alice blue", "antique white", "blue", "red", "yellow", "violet"]
step = 20
while True:
    # 0: forward
    # 1: backward
    # 2: right
    # 3: left
    tom.color(random.choice(colours))
    direction = random.randint(0, 3)
    if direction == 0:
        tom.forward(step)
    elif direction == 1:
        tom.backward(step)
    elif direction == 2:
        tom.right(90)
        tom.forward(step)
    else:
        tom.left(90)
        tom.forward(step)

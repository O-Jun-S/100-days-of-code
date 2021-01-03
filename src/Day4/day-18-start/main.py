import turtle as t
from random import choice
import random

tom = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_col = (r, g, b)
    return random_col


points = 3
while True:
    degree = 360 / points
    for i in range(points):
        tom.forward(100)
        tom.right(degree)
    tom.color(random_color())
    points += 1

import turtle as t
import random

t.colormode(255)
tom = t.Turtle()
tom.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


divide = 80
one = 360 / divide
for d in range(divide):
    tom.color(random_color())
    # tom.color("red")
    tom.circle(100)
    tom.left(one)

screen = t.Screen()
screen.exitonclick()

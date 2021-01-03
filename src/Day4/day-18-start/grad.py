import turtle as t
import random

t.colormode(255)
tom = t.Turtle()
tom.speed(0)

red = 10

divide = 100
one = 360 / divide
for d in range(divide):
    tom.color((red, 30, 70))
    tom.circle(100)
    tom.left(one)
    red += 2

screen = t.Screen()
screen.exitonclick()

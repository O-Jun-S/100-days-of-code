import turtle as t
import random

# I removed background color from extract_color's
# tuple list.
color_list = [(236, 35, 108), (221, 232, 237), (145, 28, 64),
              (239, 75, 35), (6, 148, 93), (232, 238, 234),
              (231, 168, 40), (184, 158, 46), (44, 191, 233),
              (27, 127, 195), (126, 193, 74), (253, 223, 0),
              (85, 28, 93), (173, 36, 97), (246, 219, 44),
              (44, 172, 112), (215, 130, 165), (215, 56, 27),
              (235, 164, 191), (156, 24, 23), (21, 188, 230),
              (238, 169, 157), (162, 210, 182), (138, 210, 232),
              (0, 123, 54), (88, 130, 182), (180, 187, 211)]
tom = t.Turtle()
tom.speed(0)
t.colormode(255)

left_x = -250

tom.penup()
tom.setpos(left_x, -200)

rows = 10
lines = 10
dot_size = 20
gap = 50
for line in range(lines):
    for row in range(rows):
        tom.dot(20, random.choice(color_list))
        if not row == rows - 1:
            tom.forward(gap)
    if not line == lines - 1:
        tom.left(90)
        tom.forward(gap)
        tom.right(90)
        tom.setx(left_x)

tom.hideturtle()

# end
screen = t.Screen()
screen.exitonclick()

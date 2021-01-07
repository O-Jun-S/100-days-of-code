from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")
COUNT = 3


class Counter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 40)

    def count_down(self):
        for i in range(COUNT, 0, -1):
            self.write(i, align=ALIGNMENT, font=FONT)
            time.sleep(1)
            self.clear()

from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.first_position = position
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        now_y = self.ycor()
        self.sety(now_y+20)

    def go_down(self):
        now_y = self.ycor()
        self.sety(now_y-20)

    def reset_position(self):
        self.goto(self.first_position)

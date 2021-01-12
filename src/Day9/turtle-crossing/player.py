from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.reset_position()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_finish(self):
        return self.ycor() >= FINISH_LINE_Y

    def reset_position(self):
        self.goto(STARTING_POSITION)

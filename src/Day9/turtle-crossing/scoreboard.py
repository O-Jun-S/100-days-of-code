from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT_LEVEL = "left"
ALIGNMENT_GAME_OVER = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)

        self.level = 1

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}",
                   align=ALIGNMENT_LEVEL,
                   font=FONT)

    def write_game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.",
                   align=ALIGNMENT_GAME_OVER,
                   font=FONT)

    def increase_level(self):
        self.level += 1
        self.write_level()

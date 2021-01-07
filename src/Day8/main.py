from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from counter import Counter
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My pong game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
counter = Counter()


def reset_positions_of_paddles():
    r_paddle.reset_position()
    l_paddle.reset_position()


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the top and bottom walls.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect collision with l_paddle
    elif ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect collision with the edge of the screen.
    # Detect R paddle misses.
    if ball.xcor() > 380:
        ball.reset_position()
        reset_positions_of_paddles()
        screen.update()
        scoreboard.l_point()
        counter.count_down()

    # Detect L paddle misses
    elif ball.xcor() < -380:
        ball.reset_position()
        reset_positions_of_paddles()
        screen.update()
        scoreboard.r_point()
        counter.count_down()

screen.exitonclick()

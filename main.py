from scoreboard import ScoreBoard
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


INITIAL_SPEED = 1

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
screen.listen()
scoreboard = ScoreBoard()

screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.moving_speed)
    ball.move()
    collision_counter = 0
    # Detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Ball bounces off the wall
        ball.bounce_y()
        # Detect collision with the paddle
    elif ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()
        collision_counter += 1
        ball.speed(INITIAL_SPEED + collision_counter)
        # Detect when the ball goes out of bounds
    elif ball.xcor() > 380:
        ball.restart()
        ball.moving_speed *= 1
        scoreboard.l_point()

    elif ball.xcor() < -380:
        ball.restart()
        ball.moving_speed = 0.1
        scoreboard.r_point()

screen.exitonclick()

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(fun=player.go_up, key="Up")
screen.onkey(fun=player.go_left, key="Left")
screen.onkey(fun=player.go_right, key="Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars()
    screen.update()

    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()
    if player.is_at_finish_line():
        scoreboard.increase_level()
        car_manager.increase_speed()

screen.exitonclick()

import random
from turtle import Turtle

CAR_COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_DISTANCE = 10
SPEED_INCREASE = 5


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = MOVE_DISTANCE

    def create_car(self):
        random_car = random.randint(1, 6)
        if random_car == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(CAR_COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_y = random.randint(-250, 250)
            new_car.goto(x=300, y=new_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += SPEED_INCREASE

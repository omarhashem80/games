from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.move_speed = STARTING_MOVE_DISTANCE
        self.cars = []
        self.number = 0

    def update(self):
        self.create_cars()
        self.move()

    def create_cars(self):
        if randint(0, 4) > 3 and self.number < 20:
            self.__create_car()

    def __create_car(self):
        car = Turtle()
        car.penup()
        car.color(choice(COLORS))
        car.shape("square")
        car.shapesize(stretch_len=2)
        car.setheading(180)
        car.goto(280, randint(-230, 230))
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.move_speed)
            if car.xcor() <= -310:
                self.cars.remove(car)
                car.hideturtle()
                del car

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT

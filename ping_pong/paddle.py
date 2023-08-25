from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color('white')
        self.penup()
        self.goto(x, 0)

    def up(self):
        if self.ycor() < 220:
            self.forward(40)

    def down(self):
        if self.ycor() > -220:
            self.backward(40)

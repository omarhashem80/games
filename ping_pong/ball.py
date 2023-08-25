from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.x_step = 10
        self.y_step = 10
        self.penup()
        self.shape('circle')
        self.color('white')
        self.move_speed = .1

    def move(self):
        x = self.xcor()+self.x_step
        y = self.ycor()+self.y_step
        if y > 280 or y < -280:
            self.y_step *= -1

        self.goto(x, y)

    def bounce(self):
        self.x_step *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.x_step *= -1
        self.y_step *= -1

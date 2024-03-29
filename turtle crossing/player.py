from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.showturtle()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def update(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.hideturtle()
            self.goto(STARTING_POSITION)
            self.showturtle()
            return True
        return False

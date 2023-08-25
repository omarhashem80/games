from turtle import Turtle
FONT = ("Courier", 24, "normal")
POSITION = (-120, 260)
END_POSITION = (60, 0)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.display()

    def __create_turtle(self):
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(POSITION)

    def display(self):
        self.__create_turtle()
        self.write(f"Level: {self.level}", move=False, align="right", font=FONT)

    def increment_level(self):
        self.level += 1
        self.reset()
        self.display()

    def game_over(self):
        self.goto(END_POSITION)
        self.write(f"Game Over", move=False, align="right", font=FONT)

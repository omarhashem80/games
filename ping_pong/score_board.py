from turtle import Turtle
FONT = ('Courier', 24, 'normal')
ALIGNMENT = 'center'


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 250)
        self.__display()

    def __display(self):
        self.write(f"{self.l_score}  {self.r_score}", False, align=ALIGNMENT, font=FONT)

    def increment_l_score(self):
        self.l_score += 1
        self.clear()
        self.__display()

    def increment_r_score(self):
        self.r_score += 1
        self.clear()
        self.__display()

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

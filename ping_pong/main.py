from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
from time import sleep

screen = Screen()
screen.bgcolor('black')
screen.title('Ping Pong')
screen.setup(width=800, height=600)

screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)

score_board = ScoreBoard()
ball = Ball()


screen.listen()
screen.onkey(key='Up', fun=r_paddle.up)
screen.onkey(key='Down', fun=r_paddle.down)
screen.onkey(key='w', fun=l_paddle.up)
screen.onkey(key='s', fun=l_paddle.down)

game_on = True

while game_on:
    screen.update()
    ball.move()
    sleep(ball.move_speed)
    if ball.xcor() >= 320:
        if ball.distance(r_paddle.position()) < 50 and ball.x_step > 0:
            ball.bounce()
    if ball.xcor() >= 380:
        score_board.increment_l_score()
        ball.reset_position()
    if ball.xcor() <= -320:
        if ball.distance(l_paddle.position()) < 50and ball.x_step < 0:
            ball.bounce()
    if ball.xcor() <= -380:
        score_board.increment_r_score()
        ball.reset_position()

screen.exitonclick()

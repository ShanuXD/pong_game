from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard=ScoreBoard()

screen.listen()

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)

    #check collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #check collision with right paddle
    if ball.distance(right_paddle) < 45 and ball.xcor() > 320 or ball.distance(left_paddle) < 45 and ball.xcor() < -320:
        ball.bounce_x()

    #if right paddle will miss
    if ball.xcor() > 375:
        ball.reset()
        scoreboard.left_point()
    ##if right paddle will miss
    if ball.xcor() < -375:
        ball.reset()
        scoreboard.right_point()




screen.exitonclick()

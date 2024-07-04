from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


s = Screen()
s.setup(width=800, height=600)
s.title("PONG ARCADE")
s.bgcolor("white")
s.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

s.listen()
s.onkey(r_paddle.go_up, "Up")
s.onkey(r_paddle.go_down, "Down")
s.onkey(l_paddle.go_up, "w")
s.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        #bounce
        ball.bounce_y()
    # Detect collision with right and left paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point ()
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()



s.exitonclick()

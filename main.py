from turtle import Screen
from pad1 import Paddle
from ball import Ball
from scoreboard import Scoreboard
from linea import  Linea
import time


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_pad = Paddle((350, 0))
l_pad = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
linea = Linea()


screen.listen()
#Recordar que los métodos no llevan () al momento de usarse como inputs

screen.onkey(fun=r_pad.go_up, key="Up")
screen.onkey(r_pad.go_down, "Down")
screen.onkey(l_pad.go_up, "w")
screen.onkey(l_pad.go_down, "s")

linea.drawing()

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    #Detect colision with padle
    if ball.distance(r_pad) < 50 and ball.xcor() > 320 or ball.distance(l_pad) < 50 and ball.xcor() > -320:
        ball.bounce_x()
        ball.x_move += 2
        ball.y_move += 2

    #Colisiónes con borde derecho y agregar punto
    if ball.xcor() >= 380:
        scoreboard.l_point()
        ball.x_move = 5
        ball.y_move = 5
        ball.reset_position()

    # Colisiónes con borde izquierdo y agregar punto
    if ball.xcor() <= -380:
        scoreboard.r_point()
        ball.x_move = 5
        ball.y_move = 5
        ball.reset_position()



screen.exitonclick()

from turtle import Turtle
import winsound


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.x_move = 5
        self.y_move = 5

    def move(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        winsound.PlaySound("bounce2.wav", winsound.SND_ASYNC)

    def bounce_x(self ):
        self.x_move *= -1
        winsound.PlaySound("bounce2.wav", winsound.SND_ASYNC)

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()







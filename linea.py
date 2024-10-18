from turtle import Turtle


class Linea(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.pensize(4)
        self.goto(0, -300)

    def drawing(self):
        for i in range(50):
            self.setheading(90)
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

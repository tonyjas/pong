from turtle import Turtle


class Paddle(Turtle):

    def up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        self.goto(self.xcor(), self.ycor()-20)

    def __init__(self, x_pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.goto(x_pos, 0)

from turtle import Turtle
import random

TOP_CORNER = (-435, 255)
WIDTH = 860
HEIGHT = 530


class Graphics(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()

    def border(self):
        self.goto(TOP_CORNER)
        self.pendown()
        self.pensize(2)
        self.fillcolor("darkolivegreen1")
        self.begin_fill()
        for _ in range(2):
            self.forward(WIDTH)
            self.right(90)
            self.forward(HEIGHT)
            self.right(90)
        self.end_fill()
        self.penup()

class Grass(Turtle):
    def __init__(self):
        super(Grass, self).__init__()
        self.penup()
        self.color("green")
        self.setheading(270)
        xcor = random.randrange(-430, 430, 50)
        ycor = random.randrange(-250, 250, 30)
        self.setposition(xcor, ycor)

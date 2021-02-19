from turtle import Turtle
import random

# 10 UNIT GRID WISE XCOR AND YCOR
LEFT_XCOR_LIMIT = -41
RIGHT_XCOR_LIMIT = 41
BOTTOM_YCOR_LIMIT = -26
TOP_YCOR_LIMIT = 24
GRID_UNIT = 10
colour_list = ["blue", "darkblue","firebrick1"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.4, stretch_len=0.4)
        self.penup()
        self.color("black", "blue")
        self.speed("fastest")
        xcor_food = random.randint(LEFT_XCOR_LIMIT, RIGHT_XCOR_LIMIT)
        ycor_food = random.randint(BOTTOM_YCOR_LIMIT, TOP_YCOR_LIMIT)
        self.setposition(xcor_food * GRID_UNIT, ycor_food * GRID_UNIT)

    def refresh(self):
        colour = random.choice(colour_list)
        self.color(colour)
        xcor_food = random.randint(LEFT_XCOR_LIMIT, RIGHT_XCOR_LIMIT)
        ycor_food = random.randint(BOTTOM_YCOR_LIMIT, TOP_YCOR_LIMIT)
        self.setposition(xcor_food * GRID_UNIT, ycor_food * GRID_UNIT)

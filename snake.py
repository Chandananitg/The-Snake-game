from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
LEFT_XCOR_LIMIT = -430
RIGHT_XCOR_LIMIT = 425
BOTTOM_YCOR_LIMIT = -270
TOP_YCOR_LIMIT = 250


class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_newpart(position)

    def add_newpart(self, position):
        newpart = Turtle("circle")
        if position == (0, 0):
            newpart.color("purple4")
        elif position == (-10, 0) or (-20, 0):
            newpart.color("purple3")
        else:
            newpart.color("purple1")
        newpart.shapesize(stretch_len=0.5, stretch_wid=0.5)
        newpart.penup()
        newpart.setposition(position)
        self.snake_parts.append(newpart)

    def extend(self):
        self.add_newpart(self.snake_parts[-1].position())

    def move(self):
        for part_num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part_num - 1].xcor()
            new_y = self.snake_parts[part_num - 1].ycor()
            self.snake_parts[part_num].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def is_hit_wall(self):
        if self.head.xcor() < LEFT_XCOR_LIMIT or self.head.xcor() > RIGHT_XCOR_LIMIT or self.head.ycor() < BOTTOM_YCOR_LIMIT or self.head.ycor() > TOP_YCOR_LIMIT:
            return True

    def is_hit_itself(self):
        for part in self.snake_parts[4:]:
            if self.head.distance(part) < 5:
                return True

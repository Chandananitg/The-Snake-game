from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from graphics import Graphics, Grass
import random

import time

game_is_on = True
screen = Screen()
screen.tracer(0)
screen.title("Snake")
screen.setup(width=900, height=600)
screen.bgcolor("white")

snake = Snake()
food = Food()
score = Scoreboard()
graphics = Graphics()

graphics.border()
no_of_grass = random.randint(20, 30)
# grass = []
for i in range(no_of_grass):
    grass = Grass()

screen.listen()


def stop():
    global game_is_on
    game_is_on = False


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(stop, "space")

while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.07)
    if snake.head.distance(food) < 7:
        food.refresh()
        snake.extend()
        score.score_up()

    if snake.is_hit_wall() or snake.is_hit_itself():
        game_is_on = False
        score.game_over()

screen.exitonclick()

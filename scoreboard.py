from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Comic Sans MS", 18, "normal")
SCOREBOARD_COORDINATES = (0, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(SCOREBOARD_COORDINATES)
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", align=ALIGNMENT, font=FONT)

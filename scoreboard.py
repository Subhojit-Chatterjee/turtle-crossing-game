from turtle import Turtle

SCORE_POSITION = (-275, 270)
FONT = ("Courier", 14, "normal")
GAME_OVER_FONT = ("Courier", 18, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(SCORE_POSITION)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="Center", font=GAME_OVER_FONT)

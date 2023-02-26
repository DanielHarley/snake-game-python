from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(x=0, y=260)
        self.score = -1
        self.font = ("Courier", 18, "normal")
        self.message = f"Score: {self.score}"

        self.add_score()

    def add_score(self):
        self.clear()
        self.score += 1
        self.message = f"Score: {self.score}"
        self.write(arg=self.message, move=False, align="center", font=self.font)

    def game_over(self):
        self.goto(x=0, y=0)
        self.message = "GAME OVER"
        self.write(arg=self.message, move=False, align="center", font=self.font)

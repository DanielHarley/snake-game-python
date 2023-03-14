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

        with open("high_score_record.txt") as file:
            self.high_score = int(file.read())

        self.font = ("Courier", 18, "normal")
        self.message = f"Score: {self.score}"

        self.add_score()

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("high_score_record.txt", "w") as file:
            file.write(f"{self.high_score}")
        self.message = f"Score: {self.score} High score: {self.high_score}"
        self.write(arg=self.message, move=False, align="center", font=self.font)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.message = "GAME OVER"
        self.write(arg=self.message, move=False, align="center", font=self.font)

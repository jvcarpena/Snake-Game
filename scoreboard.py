from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 15, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highest_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.teleport(0, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}, Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as f:
                f.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.teleport(0, 0)
    #     self.write(arg="GAME OVER!", align=ALIGNMENT, font=('Courier', 40, 'bold'))

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

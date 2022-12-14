from turtle import Turtle
ALIGNMENT = "center"
COLOR = "white"
FONT = ("Lucida Console", 14, "bold")


class Scoreboard(Turtle):

    score = 0
    text = f"Score: {score}"

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(COLOR)
        self.goto(0, 280)
        self.write(arg=self.text, move=False, align=ALIGNMENT, font=(FONT))

    def refresh_display(self):
        self.clear()
        self.text = f"Score: {self.score}"
        self.write(arg=self.text, move=False, align=ALIGNMENT, font=(FONT))

    def increase_score(self):
        self.score += 1
        self.refresh_display()


    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT, font=(FONT))
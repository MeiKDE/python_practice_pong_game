from turtle import Turtle

L_SCORE = 0
R_SCORE = 0

FONT = ("Courier", 80, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()  # only want it to write something
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(L_SCORE, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(R_SCORE, align=ALIGNMENT, font=FONT)

    def l_point(self):
        global L_SCORE
        L_SCORE += 1
        self.update_scoreboard()

    def r_point(self):
        global R_SCORE
        R_SCORE += 1
        self.update_scoreboard()

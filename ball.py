from turtle import Turtle

X_MOVE = 3
Y_MOVE = 3
MOVE_SPEED = 0.1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")  # making ball a circle
        self.penup()  # prevent drawing across the screen

    def move(self):
        new_x = self.xcor() + X_MOVE
        new_y = self.ycor() + Y_MOVE
        self.goto(new_x, new_y)

    def bounce_y(self):
        global Y_MOVE
        Y_MOVE *= -1  # reverse the direction of the ball

    def bounce_x(self):
        global X_MOVE, MOVE_SPEED
        X_MOVE *= -1  # reverse the direction of the ball
        MOVE_SPEED *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        global MOVE_SPEED
        MOVE_SPEED = 0.1
        self.bounce_x()

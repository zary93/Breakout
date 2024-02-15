from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        # Initialize the paddle's appearance and initial position
        super().__init__()
        self.shape('square')
        self.color('skyblue')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(x=0, y=-230)

    def go_right(self):
        # Move the paddle to the right by updating its x-coordinate
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor() )

    def go_left(self):
        # Move the paddle to the left by updating its x-coordinate
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
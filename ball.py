from turtle import Turtle


class Ball(Turtle):
    # Initialize the ball and its movement attributes
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.ball_move = 0.1

    def create_ball(self):
        # Set up the ball's appearance and initial position
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, -210)

    def move_ball(self):
        # Move the ball based on its current x and y movement attributes
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        # Reverse the x direction when the ball hits a horizontal boundary
        self.x_move *= -1

    def bounce_y(self):
        # Reverse the y direction when the ball hits a vertical boundary
        self.y_move *= -1

    def reset_ball(self):
        # Reset the ball to its initial position
        self.goto(0, -210)
import time
from tkinter import messagebox
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.bgcolor('black')
screen.setup(width=700, height=500)
screen.title("BreakOut")

paddle = Paddle()
ball = Ball()
the_wall = []
score = Score()
game_is_on = True
row = 1


def row_wall(rows):  # Create the wall with how many rows u want
    x_initial = -320
    y_position = 55
    for x in range(rows):
        for _ in range(0, 10):
            new_brick = Turtle('square')
            new_brick.color("green")
            new_brick.shapesize(stretch_wid=1, stretch_len=3)
            new_brick.penup()
            new_brick.goto(x_initial, y_position)
            the_wall.append(new_brick)
            x_initial += 70
            if y_position == 85:
                new_brick.color("yellow")
            elif y_position >= 105:
                new_brick.color('red')
        x_initial = -320
        y_position += 30


row_wall(row)

screen.listen()

screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")
while game_is_on:

    time.sleep(ball.ball_move)
    ball.move_ball()
    screen.update()
    for brick in the_wall:
        if ball.distance(brick) < 30:
            ball.bounce_y()
            brick.clear()
            brick.hideturtle()
            the_wall.remove(brick)
            score.update_score()
            if not the_wall:
                row += 1
                if row > 5:
                    game_is_on = False
                    score.update_bestscore()
                    messagebox.showinfo("Congratulation", "Great Job! You finish the game!")
                paddle.goto(0, -230)
                ball.reset_ball()
                ball.ball_move *= 0.9
                row_wall(row)
    if ball.distance(paddle) < 30 and ball.ycor() > -230:
        ball.bounce_y()
    elif ball.xcor() > 330 or ball.xcor() < -330:
        ball.bounce_x()
    elif ball.ycor() > 230:
        ball.bounce_y()
    elif ball.ycor() < -230:
        game_is_on = False
        score.update_bestscore()
        messagebox.showinfo("Game Over", f"Your score is: {score.score - 10}")


screen.exitonclick()

from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        # Initialize the Score object with default values
        self.score = 0
        # Read the best score from a file and initialize it
        with open("bestscore.txt") as data:
            score = data.read()
            if data.read() == "":
                self.bestscore = 0
            self.bestscore = int(score) - 10
        # Set up the appearance and initial position of the Score object
        self.color("white")
        self.penup()
        self.ht()
        self.goto(0, 200)
        self.update_score()

    def update_score(self):
        # Update and display the current score
        self.clear()
        self.write(arg=f"Score:{self.score} BestScore:{self.bestscore}", align='center', font=("Courier", 40, "normal"))
        self.score += 10

    def update_bestscore(self):
        # Update the best score if the current score is higher
        if self.score > self.bestscore:
            self.bestscore = self.score
            # Write the new best score to the file
            with open("bestscore.txt", mode="w") as data:
                data.write(f'{self.bestscore}')





from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("bestscore.txt") as data:
            if data.read() == "":
                self.bestscore = 0
            else:
                self.bestscore = int(data.read())
        self.color("white")
        self.penup()
        self.ht()
        self.goto(0, 200)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score:{self.score} BestScore:{self.bestscore}", align='center', font=("Courier", 40, "normal"))
        self.score += 10

    def update_bestscore(self):
        if self.score > self.bestscore:
            self.bestscore = self.score
            with open("bestscore.txt", mode="w") as data:
                data.write(f'{self.bestscore}')





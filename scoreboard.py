from turtle import Turtle, Screen

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update_score()


    def update_score(self):
        self.clear()                                    # CHANGE THESE TO CONSTANTS!
        self.write(f"Score = {self.score}", align="center", font=("Courier", 8, "normal"))


    def scoreup(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!",align="center", font=("Courier", 8, "normal"))

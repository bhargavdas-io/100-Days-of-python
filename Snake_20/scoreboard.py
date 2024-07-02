from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update()
        self.hideturtle()
    def update(self):
        self.write(f"Current Score: {self.score}", align="center", font=('arial', 10, 'bold'))
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(-25, 0)
        self.color("white")
        self.write("GAMEOVER")







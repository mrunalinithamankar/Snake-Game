from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update()
        self.hideturtle()
    
    def update(self):
        self.clear()
        self.write(f"Score:{self.score} High score:{self.high_score}",move=False,align="center", font=("Courier", 20, "normal"))

    def increment(self):
        self.score+=1
        self.update()

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as data:
                data.write(str(self.high_score))
        self.score=0
        self.update()
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game over!",move=False,align="center", font=("Courier", 20, "normal"))
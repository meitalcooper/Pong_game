from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        """Clear the current scores and update the scoreboard with new scores."""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    
    def l_point(self):
        """Increment the score for the left player and update the scoreboard.""
        self.l_score += 1
        self.update_score()
       
        
    def r_point(self):
        """Increment the score for the right player and update the scoreboard."""
        self.r_score += 1
        self.update_score()
        


from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

  
    def move(self):
        """Move the ball in the current direction by updating its x and y coordinates."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
       """Invert the y-axis movement direction."""
       self.y_move *= -1
       
    
    def bounce_x(self):
        """Invert the x-axis movement direction and slightly increase the movement speed."""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Reset the ball's position to the center and revert its movement speed to the initial state."""
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()

       
       

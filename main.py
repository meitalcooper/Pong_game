import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
difficulty_level_selected = screen.textinput(title= "Select difficulty", prompt=" Easy \n Medium \n Hared ").lower()
start_the_game  =  screen.textinput(title= "Player Controls:", prompt=" Right Player: Use the 'Up Arrow' key to move up and the 'Down Arrow' key to move down. \n Left Player: Use the 'W' key to move up and the 'S' key to move down. \n press 's' to start ").lower()
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

if difficulty_level_selected and start_the_game == 's':
    game_is_on = True
while game_is_on:
    if difficulty_level_selected == "easy":
        time.sleep(0.5)    #ball speed: 0.5  
    elif difficulty_level_selected == "medium":  #ball speed: 0.1
        time.sleep(0.1)
    elif difficulty_level_selected == "hard":    #ball speed: 0.05
        time.sleep(0.05) 
    else:
        time.sleep(0.5) # default level is easy

    screen.update()
    ball.move()

    #Detact collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detact collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        
    
    #Ditac if R paddle misses
    if ball.xcor() > 380:
       ball.reset_position()
       scoreboard.l_point()


    #Ditac if R paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

        

    





screen.exitonclick()
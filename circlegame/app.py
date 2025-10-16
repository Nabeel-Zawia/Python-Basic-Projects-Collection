from turtle import Turtle , Screen


border = Turtle()
screen = Screen()
timmy = Turtle()




def border_body():
    border.hideturtle()
    border.pensize(20)
    border.color("red")
    radius = 180
    border.circle(radius)
    return radius

def timmy_body():
    timmy.shape("circle")
    timmy.color("blue")
    timmy.penup()
    timmy.goto(timmy.xcor(),timmy.ycor()+ 180.0)



def ball_movement():
    timmy.right(90)
    timmy.forward(179)
   

game_is_on = True
circle_radius = border_body()




timmy_body()

while game_is_on:
    ball_movement()
    timmy_x = timmy.xcor()
    timmy_y = timmy.ycor()
    if timmy_x > -180 or timmy_x > 180 or timmy_y > -180 or timmy_y > 180:
        timmy.backward(380)
    

screen.exitonclick()
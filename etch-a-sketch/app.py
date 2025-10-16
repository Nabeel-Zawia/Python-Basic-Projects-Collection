from turtle import Turtle , Screen


tim = Turtle()

screen = Screen()
def move_forwards():
    tim.forward(50)
def move_backward():
    tim.backward(50)
def move_left():
    tim.left(50)
def move_right():
    tim.right(50)

tim.pensize(10)
tim.speed("fastest")
screen.listen()
screen.onkey(key="Up",fun=move_forwards)
screen.onkey(key="Down",fun=move_backward)
screen.onkey(key="Left",fun=move_left)
screen.onkey(key="Right",fun=move_right)
screen.exitonclick()

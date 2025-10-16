import colorgram
import turtle 
import random
color_list=[]

def rand_colors(colors,color_list):
    for i in colors:
        my_tuple = (i.rgb.r,i.rgb.g,i.rgb.b)
        color_list.append(my_tuple)
    print(color_list)

colors = colorgram.extract('image.jpg',12)

timmy = turtle.Turtle()
screen = turtle.Screen()
rand_colors(colors,color_list)




timmy.pensize(10)
timmy.speed("fastest")
timmy.shape("circle")

turtle.colormode(255)
timmy.penup()
timmy.setposition(-300,-300)
timmy.pendown()
for _ in range(100):
    r,g,b=random.choice(color_list)
    timmy.penup()
    timmy.forward(50)
    timmy.pendown()
    timmy.dot(20,(r,g,b))
    x,y = timmy.position()
    print(x,y)
    if x == 200:
        timmy.penup()
        timmy.setposition(-300,y + 50)
        timmy.pendown()
    if _ == 99 :
        timmy.hideturtle()

screen.exitonclick()
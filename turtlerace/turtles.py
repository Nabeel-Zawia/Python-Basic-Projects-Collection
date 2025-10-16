from turtle import Turtle
x=-230

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.penup()
timmy.goto(x,50)

kimmy = Turtle()
kimmy.shape("turtle")
kimmy.color("blue")
kimmy.penup()
kimmy.goto(x,100)

limmy = Turtle()
limmy.shape("turtle")
limmy.color("orange")
limmy.penup()
limmy.goto(x,150)

timmy.speed("slowest")
kimmy.speed("slowest")
limmy.speed("slowest")
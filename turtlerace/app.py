from turtle import Screen
import turtles
import random


screen = Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="make your bet", prompt="which turtle will when the race?? chose a color")

def motion_speed():
    speed = random.randint(1,21)
    return speed

timmy = turtles.timmy
kimmy = turtles.kimmy
limmy = turtles.limmy

is_race_on =True

winner =""
#2. TODO ILV HIATHOMI

while is_race_on:

    timmy.forward(motion_speed())
    timmy_postion = timmy.pos()
    kimmy.forward(motion_speed())
    kimmy_postion = kimmy.pos()
    limmy.forward(motion_speed())
    limmy_postion = limmy.pos()
    if timmy_postion[0] > 240:
        print("red wins")
        is_race_on=False
        winner = "red"
    elif limmy_postion[0] > 240:
        print("orange wins")
        is_race_on=False
        winner = "orange"
    elif kimmy_postion[0] > 240:
        print("blue wins")
        is_race_on=False
        winner="blue"
    else:
        pass


state =""

if user_bet.lower() == winner.lower() :
    state="won"
else:
    state="lose"
print(f"the winner is {winner} you choose ,{user_bet} so you {state}")

screen.exitonclick()
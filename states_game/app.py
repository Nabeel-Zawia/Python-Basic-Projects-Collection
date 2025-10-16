import turtle
import pandas

data = pandas.read_csv("50_states.csv")


writer = turtle.Turtle()
writer.penup()
writer.hideturtle()


screen = turtle.Screen()
screen.title("States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/ 50 Guess state" , prompt="What's your guess").title()
    if user_answer in data["state"].values:
        guessed_states.append(user_answer)
        state_row = data[data.state == user_answer]
        data_x = state_row.x.item()
        data_y = state_row.y.item()

        writer.goto(data_x, data_y)
        writer.write(user_answer)


screen.exitonclick()
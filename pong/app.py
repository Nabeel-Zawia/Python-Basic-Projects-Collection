from turtle import Turtle , Screen
import time
def middle_line():
    line = Turtle()
    line.color("white")
    line.penup()
    line.goto(x=0,y=500)
    line.right(90)
    line.pendown()
    for _ in range(50):
        line.forward(10)
        line.penup()
        line.forward(10)
        line.pendown()

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10  # speed in x direction
        self.y_move = 10  # speed in y direction

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1  # reverse vertical direction

    def bounce_x(self):
        self.x_move *= -1  # reverse horizontal direction

    def goal_scored(self, direction="left"):
        self.goto(0, 0)
        time.sleep(0.5)
        self.set_direction_towards(direction)  # set direction based on who scored

    def set_direction_towards(self, direction):
        if direction == "left":
            self.x_move = -abs(self.x_move)  # move left
            self.y_move = abs(self.y_move)  # move diagonally upwards (optional)
        elif direction == "right":
            self.x_move = abs(self.x_move)  # move right
            self.y_move = abs(self.y_move)  # move diagonally upwards (optional)
def screen_status():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=1200,height=1000)
    screen.listen()
    return screen


class first_player(Turtle):
    def __init__(self):
        super().__init__()
        
    def visibility(self):
        self.color("white")
        self.shape("square")
        self.right(90)
        self.shapesize(stretch_len=5)
        
    def position(self):
        self.penup()
        self.goto(x=-480,y=0)
    def move_up(self):
            self.backward(100)
    def move_down(self):
            self.forward(100)

    def movement(self):
        
        screen.onkey(key="Up", fun=self.move_up)
        screen.onkey(key="Down", fun=self.move_down)
        

class second_player(first_player):
    def __init__(self):
        super().__init__()
    def visibility(self):
        super().visibility()
        self.penup()
        self.goto(x=480 , y = 0)
    def movement(self):
        
        screen.onkey(key="w", fun=self.move_up)
        screen.onkey(key="s", fun=self.move_down)




class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(self.score, font=("Arial", 24, "bold"))

    def update_score(self):
        self.clear()
        self.write(self.score, font=("Arial", 24, "bold"))

class Score1(Score):
    def __init__(self):
        super().__init__(x=-30, y=460)

class Score2(Score):
    def __init__(self):
        super().__init__(x=20, y=460)



    

screen = screen_status()

paddle_1 = first_player()
paddle_2 = second_player()
paddle_1.visibility()
paddle_1.position()
paddle_2.visibility()
ball = Ball()

first_player_score = Score1()
second_player_score = Score2()

middle_line()

paddle_1.movement()
paddle_2.movement()

game_on = True
while game_on:
    screen.update()
    ball.move()
    if ball.ycor() > 480 or ball.ycor() < -480:
        ball.bounce_y()
    if ball.distance(paddle_2) < 50 and ball.xcor() > 460 or ball.distance(paddle_1) < 50 and ball.xcor() > -460:
        ball.bounce_x()
    if ball.xcor() > 490:
        first_player_score.score += 1
        first_player_score.update_score()
        ball.goal_scored(direction="left")  # Ball goes to the left corner

    elif ball.xcor() < -490:
        second_player_score.score += 1
        second_player_score.update_score()
        ball.goal_scored(direction="right")  # Ball goes to the right corner

        
screen.exitonclick()


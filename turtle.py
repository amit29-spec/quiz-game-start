import turtle
from turtle import Turtle, Screen
import random

switch = False
screen = Screen()
screen.setup(width=500, height=400)
user = screen.textinput(title="make your bet", prompt="which turtle will win the race? Enter a color: ")
colors = ['red', 'yellow', 'green', 'brown', 'blue', 'black']
dire = [-95, -55, -15, 25, 65, 95]
all_turtle = []
for index in range(0, 6):
    tim = Turtle("turtle")
    tim.color(colors[index])
    tim.penup()
    tim.goto(x=-230, y=dire[index])
    all_turtle.append(tim)
if user:
    switch = True

while switch:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            new_color = turtle.pencolor()
            switch = False
            if user == new_color:
                print("you won!")
            else:
                print(f"you loose, the winner is {new_color} turtle")

        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()

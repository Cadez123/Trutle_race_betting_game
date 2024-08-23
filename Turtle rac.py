from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)
user_guess = screen.textinput('Turtle race', 'Who do you think will win?')


turtle_list = []
color_list = ['red','blue','green','pink','magenta', 'brown']
y = -120

for color in color_list:
    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-225, y= y)
    y += 40
    turtle_list.append(new_turtle)

race = True
while race:
    for turtle in turtle_list:
        turtle.forward(random.randint(1,10))
        if turtle.xcor() >= 230:
            race = False
            winner = turtle.color()[0]
            if winner == user_guess:
                print(f'{turtle.color()[0]} turtle has won. You have won the bet')
            else:
                print(f'{turtle.color()[0]} turtle has won. You have lost the bet')

screen.exitonclick()
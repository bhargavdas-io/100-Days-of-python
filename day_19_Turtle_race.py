from turtle import Turtle, Screen
import random

s = Screen()
colors = ['red', 'blue', 'green', 'orange', 'magenta', 'black']
y_coordinates = [-120, -80, -40, 0, 40, 80]
turtles = []
s.setup(500, 400)
user_bet = s.textinput("Bet", "Which turtle will win the race? Enter a colour")

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(-235, y=y_coordinates[i])
    new_turtle.color(colors[i])
    turtles.append(new_turtle)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:

    for i in turtles:
        if i.xcor() > 230:
            is_race_on = False
            winner = i.pencolor()
            if winner == user_bet:
                print(f"You win!, {winner} wins!")
            else:
                print(f"You lost, {winner} wins!")

        rand_distance = random.randint(0, 10)
        i.forward(rand_distance)

s.exitonclick()

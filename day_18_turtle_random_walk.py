import turtle
from turtle import Turtle
from turtle import Screen
import random

t = Turtle()

turtle.colormode(255)

t.shape('circle')
t.pensize(10)
t.forward(100)
t.speed(8)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


directions = [0, 90, 180, 270]

for i in range(200):
    t.pencolor(random_colour())
    t.forward(30)
    t.setheading(random.choice(directions))

s = Screen()
s.exitonclick()

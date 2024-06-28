import turtle
from turtle import Turtle
from turtle import Screen
import random
turtle.colormode(255)


t = Turtle()
s = Screen()


def colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def spirograph(size):
    for i in range(int(360 / size)):
        t.pensize(2)
        t.speed('fastest')
        t.pencolor(colour())
        t.circle(100)
        current_heading = t.heading()
        t.setheading(current_heading + size)

spirograph(5)



s.exitonclick()

import turtle
from turtle import Turtle
from turtle import Screen
import random

#import colorgram
t = Turtle()
s = Screen()
turtle.colormode(255)

#colors = colorgram.extract("image.jpg", 30)
#color_list = []
#for i in colors:
#    color = i.rgb
#    red = color.r
#    green = color.g
#    blue = color.b
#    color_list.append((red, green, blue))
#print(color_list)

t.setheading(225)
t.penup()
t.forward(350)
t.setheading(0)
t.speed('fast')
number_of_dots = 100
colors = [(196, 175, 114),(160, 178, 194), (158, 185, 174), (191, 163, 176), (212, 205, 117), (197, 171, 49), (177, 188, 213), (203, 181, 200), (167, 209, 175), (118, 121, 186), (209, 183, 180), (170, 199, 208), (198, 206, 45)]
for i in range(1, number_of_dots +1):
    t.dot(20, random.choice(colors))
    t.hideturtle()
    t.penup()
    t.forward(50)
    if i % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)
t.hideturtle()
s.exitonclick()


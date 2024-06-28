from turtle import Turtle
from turtle import Screen
import random
tim = Turtle()
tim.shape('classic')
tim.color('Paleturquoise4')

colors = ["IndianRed", "CornflowerBlue", "DarkOrchid", "SeaGreen", "wheat", "DeepSkyBlue", "LightSeaGreen"]
def shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for i in range(3, 11):
    tim.color(random.choice(colors))
    shape(i)








#for i in range(15):
#tim.forward(10)
#tim.penup()
#tim.forward(10)
#tim.pendown()
#for i in range(4):
#tim.forward(100)
#tim.left(90)


screen = Screen()
screen.exitonclick()

from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def add_segment(self, position):
        t = Turtle("square")
        t.color("green")
        t.penup()
        t.goto(position)
        self.snakes.append(t)

    def reset(self):
        for i in self.snakes:
            i.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    def move(self):

        for i_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[i_num - 1].xcor()
            new_y = self.snakes[i_num - 1].ycor()
            self.snakes[i_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

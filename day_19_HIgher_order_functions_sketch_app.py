from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def move_forwards():
    t.forward(10)


def move_backwards():
    t.backward(10)


def counter_clockwise():
    t.lt(30)


def clockwise():
    t.rt(30)


def reset():
    t.reset()


s.listen()
s.onkey(move_forwards, "w")
s.onkey(move_backwards, "s")
s.onkey(clockwise, "d")
s.onkey(counter_clockwise, "a")
s.onkey(reset, "c")

s.exitonclick()

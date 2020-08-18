from gbsl_turtle import *

def square(width: int):
    for n in range(4):
        forward(width)
        left()


def step_down():
    right()
    forward(10)
    left()
    forward(10)


def step_up():
    forward(10)
    left()
    forward(10)
    right()


square(120)

goto(20, 90, draw=False)
square(20)

goto(80, 90, draw=False)
square(20)

goto(10, 50, draw=False)
setheading(0)

for n in range(4):
    step_down()

forward(20)

for n in range(4):
    step_up()

hideturtle()
Screen().exitonclick()

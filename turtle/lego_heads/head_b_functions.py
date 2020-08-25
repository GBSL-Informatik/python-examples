from gbsl_turtle import *


def rectangle(width: int, height: int):
    for n in range(2):
        forward(width)
        left()
        forward(height)
        left()


def square(width: int):
    rectangle(width, width)


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

goto(20, 80, draw=False)
square(20)

goto(70, 90, draw=False)
rectangle(40, 10)

goto(20, 40, draw=False)

setheading(0)

for n in range(3):
    step_down()

forward(20)

for n in range(3):
    step_up()

backward(80)

hideturtle()
Screen().exitonclick()

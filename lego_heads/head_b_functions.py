from gbsl_turtle import *

def rectangle(width: int, height: int=None):
    if height is None:
        height = width
    for n in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)

def step_down():
    right(90)
    forward(10)
    left(90)
    forward(10)


def step_up():
    forward(10)
    left(90)
    forward(10)
    right(90)

rectangle(120)

goto(20, 80, draw=False)
rectangle(20)

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

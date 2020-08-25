from gbsl_turtle import *

# Turtle Heading: ->

getturtle().speed(0)
left(18)

def circle(size: int, steps=10):
    for n in range(steps):
        forward(size)
        left(36)

circle(80)

goto(-50, 160, draw=False)
circle(10)

goto(50, 160, draw=False)
circle(10)

goto(-80, 100, draw=False)
right(90)
circle(50, steps=5)

hideturtle()
Screen().exitonclick()

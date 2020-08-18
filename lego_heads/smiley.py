from gbsl_turtle import *

# Turtle Heading: ->

left(18)
for n in range(10):
    forward(80)
    left(36)


goto(-50, 160, draw=False)
for n in range(10):
    forward(10)
    left(36)


goto(50, 160, draw=False)
for n in range(10):
    forward(10)
    left(36)

goto(-80, 100, draw=False)
right(90)

for n in range(5):
    forward(50)
    left(36)

hideturtle()
Screen().exitonclick()

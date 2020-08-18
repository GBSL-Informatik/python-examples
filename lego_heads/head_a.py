from gbsl_turtle import *

for n in range(4):
    forward(120)
    left(90)

goto(20, 90, draw=False)

for n in range(4):
    forward(20)
    left(90)

goto(80, 90, draw=False)

for n in range(4):
    forward(20)
    left(90)

goto(10, 50, draw=False)

setheading(0)

for n in range(4):
    right(90)
    forward(10)
    left(90)
    forward(10)

forward(20)

for n in range(4):
    forward(10)
    left(90)
    forward(10)
    right(90)

hideturtle()
Screen().exitonclick()

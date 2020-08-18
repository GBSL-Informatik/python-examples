from gbsl_turtle import *

for n in range(4):
    forward(120)
    left(90)

goto(20, 80, draw=False)

for n in range(4):
    forward(20)
    left(90)


goto(70, 90, draw=False)

for n in range(2):
    forward(40)
    left(90)
    forward(10)
    left(90)

goto(20, 40, draw=False)

setheading(0)

for n in range(3):
    right(90)
    forward(10)
    left(90)
    forward(10)

forward(20)

for n in range(3):
    forward(10)
    left(90)
    forward(10)
    right(90)

backward(80)

hideturtle()
Screen().exitonclick()

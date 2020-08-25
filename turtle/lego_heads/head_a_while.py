from gbsl_turtle import *

goto(0, 0, draw=False)
setheading(0)

counter = 0
while counter < 4:
    forward(120)
    left()
    counter = counter + 1

goto(20, 90, draw=False)

counter = 0
while counter < 4:
    forward(20)
    left()
    counter = counter + 1

goto(80, 90, draw=False)

counter = 0
while counter < 4:
    forward(20)
    left()
    counter = counter + 1

goto(10, 50, draw=False)

counter = 0
while counter < 4:
    right()
    forward(10)
    left()
    forward(10)
    counter = counter + 1

forward(20)

counter = 0
while counter < 4:
    forward(10)
    left()
    forward(10)
    right()
    counter = counter + 1

hideturtle()
Screen().exitonclick()

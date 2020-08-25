from gbsl_turtle import *

goto(0, 0, draw=False)
setheading(0)

counter = 0
while counter < 4:
    forward(120)
    left()
    counter = counter + 1

goto(20, 80, draw=False)

counter = 0
while counter < 4:
    forward(20)
    left()
    counter = counter + 1


goto(70, 90, draw=False)

counter = 0
while counter < 2:
    forward(40)
    left()
    forward(10)
    left()
    counter = counter + 1

goto(20, 40, draw=False)

setheading(0)

counter = 0
while counter < 3:
    right()
    forward(10)
    left()
    forward(10)
    counter = counter + 1

forward(20)

counter = 0
while counter < 3:
    forward(10)
    left()
    forward(10)
    right()
    counter = counter + 1

backward(80)

hideturtle()
Screen().exitonclick()

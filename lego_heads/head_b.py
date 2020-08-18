from gbsl_turtle import *

for _ in range(0, 4):
    forward(120)
    left(90)

penup()
goto(20, 100)
pendown()

for _ in range(0, 4):
    forward(20)
    right(90)


penup()
goto(70, 100)
pendown()

for _ in range(0, 2):
    forward(40)
    right(90)
    forward(10)
    right(90)

penup()
goto(20, 40)
pendown()

setheading(0)

for _ in range(0, 3):
    right(90)
    forward(10)
    left(90)
    forward(10)

forward(20)

for _ in range(0, 3):
    forward(10)
    left(90)
    forward(10)
    right(90)

backward(80)

hideturtle()
Screen().exitonclick()

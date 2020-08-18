from gbsl_turtle import *

for _ in range(0, 4):
    forward(120)
    left(90)

penup()
goto(20, 110)
pendown()

for _ in range(0, 4):
    forward(20)
    right(90)

penup()
goto(80, 110)
pendown()

for _ in range(0, 4):
    forward(20)
    right(90)

penup()
goto(10, 50)
pendown()

setheading(0)

for _ in range(0, 4):
    right(90)
    forward(10)
    left(90)
    forward(10)

forward(20)

for _ in range(0, 4):
    forward(10)
    left(90)
    forward(10)
    right(90)

hideturtle()
Screen().exitonclick()

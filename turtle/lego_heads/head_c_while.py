from gbsl_turtle import *

goto(-40, 0, draw=False)
Screen().tracer(2)

counter = 0
while counter < 8:
    forward(80)
    left(45)
    counter = counter + 1

goto(-30, 140, draw=False)
setheading(180)     # Orientierung nach links: ◀️

counter = 0
while counter < 8:
    forward(10)
    right(45)
    counter = counter + 1


goto(30, 140, draw=False)
setheading(0)       # Orientierung nach rechts: ▶️


counter = 0
while counter < 8:
    forward(10)
    left(45)
    counter = counter + 1


goto(0, 80, draw=False)
setheading(22.5)

counter = 0
while counter < 8:
    forward(8)
    left(45)
    counter = counter + 1

goto(-72, 60, draw=False)
setheading(-45)     # Orientierung nach rechts unten: ↘️

counter = 0
while counter < 3:
    forward(60)
    left(45)
    counter = counter + 1

hideturtle()
Screen().exitonclick()

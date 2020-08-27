from gbsl_turtle import *

goto(-40, 0, draw=False)
Screen().tracer(2)

for counter in range(8):
    forward(80)
    left(45)

goto(-30, 140, draw=False)
setheading(180)     # Orientierung nach links: ◀️

for counter in range(8):
    forward(10)
    right(45)


goto(30, 140, draw=False)
setheading(0)       # Orientierung nach rechts: ▶️


for counter in range(8):
    forward(10)
    left(45)


goto(0, 80, draw=False)
setheading(22.5)

for counter in range(8):
    forward(8)
    left(45)

goto(-72, 60, draw=False)
setheading(-45)     # Orientierung nach rechts unten: ↘️

for counter in range(3):
    forward(60)
    left(45)

hideturtle()
Screen().exitonclick()

from gbsl_turtle import *

goto(-30, 0, draw=False)

counter = 0
while counter < 8:
    forward(60)
    left(45)
    counter = counter + 1

goto(-30, 100, draw=False)
setheading(180)     # Orientierung nach links: ◀️

counter = 0
while counter < 8:
    forward(5)
    right(45)
    counter = counter + 1


goto(30, 100, draw=False)
setheading(0)       # Orientierung nach rechts: ▶️


counter = 0
while counter < 8:
    forward(5)
    left(45)
    counter = counter + 1


goto(-48, 40, draw=False)
setheading(-45)     # Orientierung nach rechts unten: ↘️

counter = 0
while counter < 3:
    forward(40)
    left(45)
    counter = counter + 1

done()

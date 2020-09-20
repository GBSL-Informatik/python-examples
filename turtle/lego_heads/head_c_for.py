from gbsl_turtle import *

goto(-30, 0, draw=False)

for counter in range(8):
    forward(60)
    left(45)

goto(-30, 100, draw=False)
setheading(180)     # Orientierung nach links: ◀️

for counter in range(8):
    forward(5)
    right(45)


goto(30, 100, draw=False)
setheading(0)       # Orientierung nach rechts: ▶️


for counter in range(8):
    forward(5)
    left(45)


goto(-48, 40, draw=False)
setheading(-45)     # Orientierung nach rechts unten: ↘️

for counter in range(3):
    forward(40)
    left(45)

done()

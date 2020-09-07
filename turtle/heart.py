from gbsl_turtle import *

fillcolor('red')
pencolor('red')
speed(10)

# Start filling the color
begin_fill()

# Draw the left line
left(140)
forward(113)
for counter in range(200):
    forward(1)
    right(1)

left(120)

for a in [1, 2, 3]:
    print(a)

for counter in range(200):
    forward(1)
    right(1)
Screen().tracer(1)

forward(112)
end_fill()
Screen().update()
done()

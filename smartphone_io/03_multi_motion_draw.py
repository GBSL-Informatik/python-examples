from smartphone_connector import *
from gbsl_turtle import *

phone = Connector("https://io.gbsl.website", "FooBar")

Screen().tracer(1, 0)

tim = Turtle()
jon = Turtle()
maria = Turtle()
joana = Turtle()

turtles = [tim, jon, joana, maria]
jon.setheading(180)
maria.setheading(90)
joana.setheading(-90)
tim.pencolor('red')
jon.pencolor('blue')
maria.pencolor('yellow')
joana.pencolor('green')
for t in turtles:
    t.pensize(3)


def on_f1():
    for t in turtles:
        t.penup()
        t.home()
        t.pendown()
    jon.setheading(180)


def on_f2():
    for t in turtles:
        t.home()
        t.clear()


phone.on_f1 = on_f1
phone.on_f2 = on_f2


def on_update(data: DataFrame):
    if data.acceleration.x > 2:
        for t in turtles:
            t.left(2)
    elif data.acceleration.x < -2:
        for t in turtles:
            t.right(2)
    for t in turtles:
        t.forward(2)


# phone.set_update_interval(0.1)
phone.subscribe(on_update, interval=0.01)

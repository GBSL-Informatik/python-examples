from smartphone_connector import *
from gbsl_turtle import *
from math import sqrt

phone = Connector("https://io.gbsl.website", "FooBar")

home()
Screen().tracer(2, 0)


def on_f1():
    home(draw=False)


def on_f2():
    print('clear')
    clear()
    home(draw=False)


phone.on_f1 = on_f1
phone.on_f2 = on_f2


def on_update(data: DataFrame):
    if data.acceleration.x > 2:
        left(2)
    elif data.acceleration.x < -2:
        right(2)
    forward(2)


# phone.set_update_interval(0.1)
phone.subscribe(on_update, interval=0.01)

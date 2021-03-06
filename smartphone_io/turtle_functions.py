from smartphone_connector import *
from gbsl_turtle import *
import random

phone = Connector("https://io.gbsl.website", "FooBar")

home()


def on_f1():
    for _ in range(4):
        forward(100)
        left(90)


def on_f2():
    for _ in range(9):
        forward(30)
        left(360 / 9)


def on_f3():
    for _ in range(5):
        forward(100)
        left(144)


def on_f4():
    goto(random.randint(-250, 250), random.randint(-250, 250), draw=False)


phone.on_f1 = on_f1
phone.on_f2 = on_f2
phone.on_f3 = on_f3
phone.on_f4 = on_f4

Screen().mainloop()

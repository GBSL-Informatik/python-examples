from smartphone_connector import Connector, random_color
import random

phone = Connector('https://io.gbsl.website', 'FooBar')


def on_pointer(data, phone: Connector):
    phone.set_color(random_color())


phone.on_pointer = on_pointer

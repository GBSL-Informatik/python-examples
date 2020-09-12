from smartphone_connector import Connector, random_color
import random

phone = Connector('https://io.gbsl.website', 'FooBar')

while True:
    phone.set_color(random_color())
    phone.sleep(0.05)

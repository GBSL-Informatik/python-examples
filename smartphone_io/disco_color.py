from smartphone_connector import Connector, random_color
import random

connector = Connector('https://io.gbsl.website', 'FooBar')

while True:
    connector.set_color(random_color())
    connector.sleep(0.05)
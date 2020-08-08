from smartphone_connector import Connector, random_color
import random

connector = Connector('https://io.balthasarhofer.ch', 'FooBar')

def on_pointer(data, connector: Connector):
    connector.set_color(random_color())

connector.on_pointer = on_pointer
from smartphone_connector import Connector, random_color, ColorPointer
from random import uniform

phone = Connector("https://io.gbsl.ch", "FooBar")

def on_pointer(key: ColorPointer):
    if key.type != 'pointer':
        return
    print(f'reaction time: {key.time_stamp - key.displayed_at}s')

phone.on_pointer = on_pointer
while True:
    phone.set_color(random_color())
    phone.sleep(uniform(1, 7))

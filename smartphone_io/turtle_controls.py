from gbsl_turtle import *
from smartphone_connector import Connector, KeyMsg
import time

# visit https://io.gbsl.website/controller?device_id=FooBar


def on_key(data: KeyMsg):
    if data.key == 'up':
        forward()
    elif data.key == 'right':
        right()
    elif data.key == 'left':
        left()
    elif data.key == 'down':
        backward()
    Screen().update()

connector = Connector('https://io.gbsl.website', 'FooBar')
connector.on_key = on_key
Screen().mainloop()
connector.disconnect()
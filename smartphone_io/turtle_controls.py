from gbsl_turtle import *
from smartphone_connector import *


def on_key(data: KeyMsg):
    print(data.key)
    if data.key == 'up':
        forward()
    elif data.key == 'right':
        right()
    elif data.key == 'left':
        left()
    elif data.key == 'down':
        backward()
    Screen().update()


phone = Connector('https://io.gbsl.website', 'FooBar')
phone.on_key = on_key

Screen().mainloop()
phone.disconnect()

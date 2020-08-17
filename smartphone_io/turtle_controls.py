from turtle import Turtle, Screen, _Screen
from smartphone_connector import Connector, KeyMsg
import time

# visit https://io.gbsl.website/controller?device_id=FooBar

jack = Turtle()
screen: _Screen = jack.screen

def on_key(data: KeyMsg):
    if data.key == 'up':
        jack.forward(10)
    elif data.key == 'right':
        jack.right(90)
    elif data.key == 'left':
        jack.left(90)
    elif data.key == 'down':
        jack.backward(10)
    screen.update()

connector = Connector('https://io.gbsl.website', 'FooBar')
connector.on_key = on_key
screen.mainloop()
connector.disconnect()
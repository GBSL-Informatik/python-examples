from turtle import Turtle, Screen, _Screen
from smartphone_connector import Connector
import time, webbrowser

# visit https://io.balthasarhofer.ch/controller?deviceId=FooBar
webbrowser.open_new_tab('https://io.balthasarhofer.ch/controller?deviceId=FooBar')

jack = Turtle()
screen: _Screen = jack.screen

def on_key(data):
    print('new data received with ', data)
    if data['type'] == 'key':
        if data['key'] == 'up':
            jack.forward(10)
        elif data['key'] == 'right':
            jack.right(90)
        elif data['key'] == 'left':
            jack.left(90)
        elif data['key'] == 'down':
            jack.backward(10)
        screen.update()

connector = Connector('https://io.balthasarhofer.ch', 'FooBar')
screen.mainloop()
connector.disconnect()
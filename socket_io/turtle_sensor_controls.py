from turtle import Turtle, Screen, _Screen
from smartphone_connector import Connector
import time

# visit https://io.balthasarhofer.ch/controller?deviceId=FooBar

jack = Turtle()
jack.speed(0)
screen: _Screen = jack.screen
screen.tracer(0, 0)
doing = False
connector = Connector('https://io.balthasarhofer.ch', 'FooBar')

lastTimeStamp = 0

def turtle_step():
    global lastTimeStamp, jack, screen, connector
    data = connector.latest_data(data_type='acceleration')
    if data is None:
        return
    lastTimeStamp = data['timeStamp']
    accX = data['acceleration']['x']
    
    step_size = 2
    angle = 0
    if accX > 1:
        angle = step_size
    elif accX < -1:
        angle = -step_size

    jack.left(angle)
    jack.forward(step_size)

    screen.update()

try:
    while True:
        time.sleep(0.01)
        turtle_step()

finally:
    connector.disconnect()
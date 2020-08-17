from turtle import Turtle, Screen, _Screen
from smartphone_connector import Connector
import time

# visit https://io.gbsl.website/controller?device_id=FooBar

jack = Turtle()
jack.speed(0)
screen: _Screen = jack.screen
screen.tracer(0, 0)
doing = False
connector = Connector('https://io.gbsl.website', 'FooBar')
go_home = False

def on_key(data):
    global go_home
    if data['key'] == 'home':
        go_home = True

connector.on_key = on_key

def turtle_step(jack: Turtle, connector: Connector):
    data = connector.latest_acceleration()
    if data is None:
        return
    
    step_size = 2
    angle = 0
    if data.x > 1:
        angle = step_size
    elif data.x < -1:
        angle = -step_size

    jack.left(angle)
    jack.forward(step_size)

    jack.screen.update()


try:
    while True:
        time.sleep(0.01)
        if go_home:
            jack.home()
            jack.screen.update()
            go_home = False
        turtle_step(jack, connector)
except:
    pass

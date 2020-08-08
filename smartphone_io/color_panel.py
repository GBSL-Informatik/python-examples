from smartphone_connector import Connector
import time

# visit https://io.balthasarhofer.ch/color_panel?device_id=FooBar
connector = Connector('https://io.balthasarhofer.ch', 'FooBar')
for color in ['red', 'green', 'blue']:
    print('set color: ', color)
    connector.set_color(color)
    time.sleep(1)
connector.disconnect()

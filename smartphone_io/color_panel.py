from smartphone_connector import Connector
import time

# visit https://io.gbsl.website/color_panel?device_id=FooBar
phone = Connector('https://io.gbsl.website', 'FooBar')
for color in ['red', 'green', 'blue']:
    print('set color: ', color)
    phone.set_color(color)
    time.sleep(1)
phone.disconnect()

from smartphone_connector import Connector
import time, webbrowser

# visit https://io.balthasarhofer.ch/color_panel?deviceId=FooBar
webbrowser.open_new_tab('https://io.balthasarhofer.ch/controller?deviceId=FooBar')
connector = Connector('https://io.balthasarhofer.ch', 'FooBar')
for color in ['red', 'green', 'blue']:
    print('set color: ', color)
    connector.set_color(color)
    time.sleep(1)
connector.disconnect()

from smartphone_connector import Connector
connector = Connector('https://io.balthasarhofer.ch', 'FooBar')

def blink(device_nr: int, connector: Connector):
    connector.set_color('red', unicast_to=device_nr)
    connector.sleep(1)
    connector.set_color('black', unicast_to=device_nr)


connector.set_color('black', broadcast=True)
while True:
    for device in connector.client_devices:
        blink(device['device_nr'], connector)

connector.wait()

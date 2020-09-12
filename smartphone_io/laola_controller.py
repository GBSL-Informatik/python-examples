from smartphone_connector import Connector
phone = Connector('https://io.gbsl.website', 'FooBar')


def blink(device_nr: int, phone: Connector):
    phone.set_color('red', unicast_to=device_nr)
    phone.sleep(1)
    phone.set_color('black', unicast_to=device_nr)


phone.set_color('black', broadcast=True)
while True:
    for device in phone.client_devices:
        blink(device['device_nr'], phone)

phone.wait()

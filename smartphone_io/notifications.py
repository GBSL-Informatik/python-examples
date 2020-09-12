from smartphone_connector import Connector

# phone = Connector('http://localhost:5000', 'FooBar')
phone = Connector('https://io.gbsl.website', 'FooBar')

name = phone.prompt('Name?', input_type='datetime')
phone.notify(f'Hello Dude {name}', display_time=2, broadcast=True)
phone.sleep(1)
phone.disconnect()

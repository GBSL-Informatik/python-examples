from smartphone_connector import Connector

# connector = Connector('http://localhost:5000', 'FooBar')
connector = Connector('https://io.gbsl.website', 'FooBar')

name = connector.prompt('Name?', input_type='datetime')
connector.notify(f'Hello Dude {name}', display_time=2, broadcast=True)
connector.sleep(1)
connector.disconnect()

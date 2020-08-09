# %% [markdown]
# # Instruktion
# Alle SuS haben auf ihrem Laptop folgendes Skript, mit ihrer eigenen Device-ID
# Alle Handys Als Kreis in der Mitte.
# Sobald jemand ein Display berührt, wird die Farbe im Kreis rumgegeben

# %%
from smartphone_connector import Connector, random_color, Device
connector = Connector('https://io.balthasarhofer.ch', 'FooBar')


def blink(device: Device, color: str, connector: Connector):
    connector.set_color(color)
    connector.sleep(1)
    connector.set_color('black')

    connector.broadcast({
        'type': 'next_nr',
        'next_nr': device.device_nr + 1,
        'color': color
    })


def on_data(data, connector: Connector):
    device = connector.client_device
    if device is None:
        return

    if data.type == 'next_nr':

        # # zusatz: handys im kreis, und die farbe im Kreis ringsumgeben...
        # # --> erstes gerät muss auch auf "letzte" nummer hören!
        # is_first = device.device_nr == 0
        # is_my_turn = data.next_nr == device.device_nr or (is_first and data.next_nr == connector.client_count)

        is_my_turn = data.next_nr == device.device_nr
        if is_my_turn:
            blink(device, data.color, connector)
    if data.type == 'pointer':
        blink(device, random_color(), connector)


connector.on_data = on_data
connector.set_color('black', broadcast=True)
connector.wait()

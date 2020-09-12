# %% [markdown]
# # Instruktion
# Alle SuS haben auf ihrem Laptop folgendes Skript, mit ihrer eigenen Device-ID
# Alle Handys Als Kreis in der Mitte.
# Sobald jemand ein Display berührt, wird die Farbe im Kreis rumgegeben

# %%
from smartphone_connector import Connector, random_color, Device
phone = Connector('https://io.gbsl.website', 'FooBar')


def blink(device: Device, color: str, phone: Connector):
    phone.set_color(color)
    phone.sleep(1)
    phone.set_color('black')

    phone.broadcast({
        'type': 'next_nr',
        'next_nr': device.device_nr + 1,
        'color': color
    })


def on_data(data, phone: Connector):
    device = phone.client_device
    if device is None:
        return

    if data.type == 'next_nr':

        # # zusatz: handys im kreis, und die farbe im Kreis ringsumgeben...
        # # --> erstes gerät muss auch auf "letzte" nummer hören!
        # is_first = device.device_nr == 0
        # is_my_turn = data.next_nr == device.device_nr or (is_first and data.next_nr == phone.client_count)

        is_my_turn = data.next_nr == device.device_nr
        if is_my_turn:
            blink(device, data.color, phone)
    if data.type == 'pointer':
        blink(device, random_color(), phone)


phone.on_data = on_data
phone.set_color('black', broadcast=True)
phone.wait()

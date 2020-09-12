from smartphone_connector import *

name = [
    '9  9 9999 9   9 9999 9    9     97079     ',
    '9  9 9  9 99  9 9    9    9    9897889    ',
    '9999 9999 9 9 9 9999 9    9     98689     ',
    '9  9 9  9 9  99    9 9    9      989      ',
    '9  9 9  9 9   9 9999 9999 9       9       '
]
phone = Connector("https://io.gbsl.website", "FooBar")

while True:
    phone.set_image(name)
    for idx, row in enumerate(name, 0):
        name[idx] = row[1:] + row[0]
    phone.sleep(0.1)

from smartphone_connector import Connector
from itertools import cycle, tee

text = [
    [9, 0, 0, 9, 0, 9, 9, 9, 9, 0, 9, 0, 0, 0, 9, 0, 0, 0, 9, 9, 9, 9, 0, 0, 0, 0],
    [9, 0, 0, 9, 0, 9, 0, 0, 9, 0, 9, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 9, 0, 0, 0, 0],
    [9, 9, 9, 9, 0, 9, 9, 9, 9, 0, 9, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 9, 0, 0, 0, 0],
    [9, 0, 0, 9, 0, 9, 0, 0, 9, 0, 9, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 9, 0, 0, 0, 0],
    [9, 0, 0, 9, 0, 9, 0, 0, 9, 0, 9, 9, 9, 0, 9, 9, 9, 0, 9, 9, 9, 9, 0, 0, 0, 0]
]

c = cycle(zip(*text))
window = 15
cycles = tee(c, window)
for i in range(window):
    for r in range(i):
        next(cycles[i])

phone = Connector("https://io.gbsl.website", 'FooBar')

while True:
    image = []
    for cy in cycles:
        image.append(next(cy))
    image = list(map(list, zip(*image)))
    phone.set_grid(image)
    phone.sleep(0.2)

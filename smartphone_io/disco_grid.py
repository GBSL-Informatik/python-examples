from smartphone_connector import Connector, random_color
import random

phone = Connector('https://io.gbsl.website', 'FooBar')

while True:
    columns = random.randint(50, 100)
    rows = random.randint(50, 100)
    grid = []
    for _ in range(0, rows):
        row = []
        for _ in range(0, columns):
            row.append(random_color())
        grid.append(row)
    phone.set_grid(grid)
    phone.sleep(0.75)

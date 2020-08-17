from smartphone_connector import Connector, random_color
import random

connector = Connector('https://io.gbsl.website', 'FooBar')

while True:
    columns = random.randint(50, 100)
    rows = random.randint(50, 100)
    grid = []
    for _ in range(0, rows):
        row = []
        for _ in range(0, columns):
            row.append(random_color())
        grid.append(row)
    connector.set_grid(grid)
    connector.sleep(0.75)

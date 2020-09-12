from smartphone_connector import Connector, random_color, GridPointer
import random

phone = Connector('https://io.gbsl.website', 'FooBar')

grid = []
for _ in range(0, 9):
    row = []
    for _ in range(0, 3):
        row.append(random_color())
    grid.append(row)


def on_pointer(data: GridPointer, phone: Connector):
    global grid
    grid[data.row][data.column] = random_color()
    phone.set_grid(grid)


phone.on_pointer = on_pointer
phone.set_grid(grid)

from smartphone_connector import Connector, random_color, GridPointer
import random

connector = Connector('https://io.gbsl.website', 'FooBar')

grid = []
for _ in range(0, 9):
    row = []
    for _ in range(0, 3):
        row.append(random_color())
    grid.append(row)

def on_pointer(data: GridPointer, connector: Connector):
    global grid
    grid[data.row][data.column] = random_color()
    connector.set_grid(grid)

connector.on_pointer = on_pointer
connector.set_grid(grid)
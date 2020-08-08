from smartphone_connector import Connector, random_color, PointerMsg
import random

connector = Connector('https://io.balthasarhofer.ch', 'FooBar')

grid = []
for _ in range(0, 9):
    row = []
    for _ in range(0, 3):
        row.append(random_color())
    grid.append(row)

def on_pointer(data: PointerMsg, connector: Connector):
    global grid
    pointer = data['pointer']
    grid[pointer['row']][pointer['column']] = random_color()
    connector.set_grid(grid)

connector.on_pointer = on_pointer
connector.set_grid(grid)
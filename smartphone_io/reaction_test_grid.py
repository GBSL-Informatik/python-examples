from smartphone_connector import Connector, GridPointer
from random import randint
from typing import List

phone = Connector("https://io.gbsl.website", "FooBar")


def get_grid():
    grid = [
        ['black', 'black', 'black', 'black'],
        ['black', 'black', 'black', 'black'],
        ['black', 'black', 'black', 'black'],
        ['black', 'black', 'black', 'black']
    ]
    for _ in range(2):
        row = randint(0, 3)
        col = randint(0, 3)
        grid[row][col] = 'red'
    return grid

grid = get_grid()
displayed_at = None

def is_done(grid: List[List[str]]) -> bool:
    for row in grid:
        for col in row:
            if col == 'red':
                return False
    return True

def on_pointer(key: GridPointer):
    global grid
    global displayed_at
    if key.type != 'pointer' or key.context != 'grid':
        return
    grid[key.row][key.column] = 'gray'
    if displayed_at is None:
        displayed_at = key.displayed_at

    if is_done(grid):
        grid = get_grid()
        print(f'-- finished in: {key.time_stamp - displayed_at}s')
        displayed_at = None
    else:
        print(f'duration: {key.time_stamp - displayed_at}s')

    phone.set_grid(grid)


phone.on_pointer = on_pointer
phone.set_grid(grid)

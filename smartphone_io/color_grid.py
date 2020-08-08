from smartphone_connector import Connector
import time
URL = 'https://io.balthasarhofer.ch'
# visit https://io.balthasarhofer.ch/color_grid?device_id=FooBar

def get_checker_board(first_white = True, size=8):
    board = []
    size2 = size // 2
    for _ in range(0, size2):
        board.append(['white', 'black'] * size2)
        board.append(['black', 'white'] * size2)

    if not first_white:
        board.reverse()
    return board

connector = Connector(URL, 'FooBar')
for i in range(0, 10):
    for start_white in [True, False]:
        connector.set_grid(get_checker_board(start_white, size=32))
        print('set checker board')
        time.sleep(0.5)
connector.disconnect()

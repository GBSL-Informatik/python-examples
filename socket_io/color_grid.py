from smartphone_connector import Connector
import time, webbrowser
# URL = 'https://io.balthasarhofer.ch'
URL = 'http://localhost:5000'
# visit https://io.balthasarhofer.ch/color_grid?deviceId=FooBar
# webbrowser.open_new_tab(f'{URL}/color_grid?deviceId=FooBar')

def getCheckerBoard(first_white = True):
    board = []
    for i in range(0, 8):
        start_white = i % 2 == 0
        if not first_white:
            start_white = not start_white
        
        if start_white:
            board.append(['white', 'black', 'white', 'black', 'white', 'black', 'white', 'black'])
        else:
            board.append(['black', 'white', 'black', 'white', 'black', 'white', 'black', 'white'])

    return board

connector = Connector(URL, 'FooBar')
for i in range(0, 1):
    for start_white in [True, False]:
        connector.set_grid(getCheckerBoard(start_white))
        print('set checker board')
        time.sleep(0.5)
connector.disconnect()

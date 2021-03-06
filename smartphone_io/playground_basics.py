from smartphone_connector import Connector, DictX, KeyMsg, AccMsg, random_color
from random import randint


device = Connector('https://io.gbsl.website', 'FooBar')
player = DictX({
  'color': 'yellow',
  'form': 'round',
  'height': 10,
  'width': 10,
  'id': 'player1',
  'movement': 'controlled',
  'pos_x': 0,
  'pos_y': 0
})


def on_key(data: KeyMsg):
    if data.key == 'right':
        player.pos_x += 5
        device.update_sprite('player1', {'pos_x': player.pos_x})
    if data.key == 'left':
        player.pos_x -= 5
        device.update_sprite('player1', {'pos_x': player.pos_x})
    if data.key == 'up':
        player.pos_y += 5
        device.update_sprite('player1', {'pos_y': player.pos_y})
    if data.key == 'down':
        player.pos_y -= 5
        device.update_sprite('player1', {'pos_y': player.pos_y})
    if data.key == 'home':
        if player.form == 'round':
            player.form = 'rectangle'
        else:
            player.form = 'round'
        device.update_sprite('player1', {'form': player.form})


positions = [(0, 0)]


def update_position(dx: float, dy: float):
    new_x = positions[-1][0] - dx / 2
    new_y = positions[-1][1] - dy / 2
    if new_x > 98:
        new_x = 98
    elif new_x < 0:
        new_x = 0
    if new_y > 198:
        new_y = 198
    elif new_y < 0:
        new_y = 0
    positions.append((new_x, new_y))


def on_acc(data: AccMsg):
    global positions
    update_position(data.x, data.y)
    device.update_sprite('player1', {
        'pos_x': positions[-1][0],
        'pos_y': positions[-1][1],
    })
    if len(positions) >= 20:
        device.update_sprite('player2', {
            'pos_x': positions[-20][0],
            'pos_y': positions[-20][1],
        })
    if len(positions) >= 40:
        device.update_sprite('player3', {
            'pos_x': positions[-40][0],
            'pos_y': positions[-40][1],
        })
    # updates = [{
    #     'id': 'player1',
    #     'movement': 'controlled',
    #     'pos_x': positions[-1][0],
    #     'pos_y': positions[-1][1],
    # }]
    # if len(positions) >= 200:
    #     updates.append({
    #         'id': 'player2',
    #         'movement': 'controlled',
    #         'pos_x': positions[-200][0],
    #         'pos_y': positions[-200][1],
    #     })
    # if len(positions) >= 400:
    #     updates.append({
    #         'id': 'player3',
    #         'movement': 'controlled',
    #         'pos_x': positions[-400][0],
    #         'pos_y': positions[-400][1],
    #     })

    # device.add_sprites(updates)


device.on_key = on_key
device.on_sprite_collision = lambda data: print(data)
device.configure_playground({
        'width': 100,
        'height': 200,
        'shift_x': 0,
        'shift_y': 0
    })

device.add_sprites([
    {
        'color': 'yellow',
        'form': 'round',
        'height': 10,
        'width': 10,
        'id': 'player1',
        'movement': 'controlled',
        'pos_x': 0,
        'pos_y': 0
    },
    {
        'color': 'yellow',
        'form': 'round',
        'height': 7,
        'width': 7,
        'id': 'player2',
        'movement': 'controlled',
        'pos_x': 50,
        'pos_y': 50
    },
    {
        'color': 'yellow',
        'form': 'round',
        'height': 4,
        'width': 4,
        'id': 'player3',
        'movement': 'controlled',
        'pos_x': 70,
        'pos_y': 70
    }
])

device.on_acceleration = on_acc

sprite_count = 0
while True:
    sprite_count += 1
    device.sleep(0.5)
    w = randint(2, 10)
    device.add_sprite({
        'color': random_color(),
        'direction': [0, -1],
        'form': 'round',
        'height': randint(2, 10),
        'width': w,
        'id': f'asdfa{sprite_count}',
        'movement': 'uncontrolled',
        'pos_x': randint(0, 100 - w),
        'pos_y': 200,
        'speed': randint(1, 60) / 10
    })

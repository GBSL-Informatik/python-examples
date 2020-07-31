from pynput import keyboard
import time
import sys

THRESHOLD_TO_RESET = 5
CURSOR_UP_KEY = '\033[F'
DELETE_LINE_KEY = '\033[K'

input_characters = []
start_time = 0
last_keystroke_time = 0.0
error_count = 0


def get_stats():
    global last_keystroke_time, error_count, input_characters
    duration = (last_keystroke_time - start_time) / 60.0

    if duration == 0:
        duration = 1

    keystroke_count = len(input_characters)
    stats = f'Tastenanschläge/Minute: {keystroke_count / duration}'
    return stats


def reset_stats():
    global start_time, input_characters
    start_time = time.time()
    input_characters = []


def print_output():
    stats = get_stats()
    print(f'{CURSOR_UP_KEY}{DELETE_LINE_KEY}{stats}')
    sys.stdout.flush()


def on_press(key):
    global input_characters, last_keystroke_time, start_time

    if last_keystroke_time - start_time > THRESHOLD_TO_RESET:
        reset_stats()

    last_keystroke_time = time.time()
    try:
        current_char = key.char
        input_characters.append(current_char)
    except AttributeError:
        if key == keyboard.Key.esc:
            return False
        input_characters.append(key)

    print_output()


print('Start Keylogger... Press "esc" to quit')
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

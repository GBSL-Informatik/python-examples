from smartphone_connector import Connector
MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': ' '
}


def translate(text: str):
    morsed = []
    for char in text:
        morse_code = MORSE_CODE_DICT[char.upper()]
        morsed.append(morse_code)
    return morsed


phone = Connector('https://io.gbsl.website', 'FooBar')

codes = translate('Hallo Schatz')

for code in codes:
    print(code)
    if code == '.':
        phone.set_color('red')
        phone.sleep(0.5)
        phone.set_color('black')
        phone.sleep(0.5)
    if code == '-':
        phone.set_color('red')
        phone.sleep(1.5)
        phone.set_color('black')
        phone.sleep(0.5)
    if code == ' ':
        phone.set_color('pink')
        phone.sleep(2)
        phone.set_color('black')
        phone.sleep(0.5)

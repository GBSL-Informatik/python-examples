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


connector = Connector('https://io.gbsl.website', 'FooBar')

codes = translate('Hallo Schatz')

for code in codes:
    print(code)
    if code == '.':
        connector.set_color('red')
        connector.sleep(0.5)
        connector.set_color('black')
        connector.sleep(0.5)
    if code == '-':
        connector.set_color('red')
        connector.sleep(1.5)
        connector.set_color('black')
        connector.sleep(0.5)
    if code == ' ':
        connector.set_color('pink')
        connector.sleep(2)
        connector.set_color('black')
        connector.sleep(0.5)

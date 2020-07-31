from gtts import gTTS
from playsound import playsound


def to_gruefnisch(text: str):
    text = text.lower()
    text = text.replace('a', 'anafa')
    text = text.replace('e', 'enefe')
    text = text.replace('i', 'inifi')
    text = text.replace('o', 'onofo')
    text = text.replace('u', 'unufu')
    text = text.replace('ä', 'änäfä')
    text = text.replace('ö', 'önöfö')
    text = text.replace('ü', 'ünüfü')
    return text


def from_gruefnisch(text: str):
    text = text.lower()
    text = text.replace('anafa', 'a')
    text = text.replace('enefe', 'e')
    text = text.replace('inifi', 'i')
    text = text.replace('onofo', 'o')
    text = text.replace('unufu', 'u')
    text = text.replace('änäfä', 'ä')
    text = text.replace('önöfö', 'ö')
    text = text.replace('ünüfü', 'ü')
    return text


def speak(text: str):
    myobj = gTTS(text=text, lang='de', slow=False)
    myobj.save("speak_out.mp3")
    playsound("speak_out.mp3")


def what_to_do():
    print('Was möchten Sie machen?')
    print()
    print('(a) Normal zu Grüfnisch übersetzen')
    print('(b) Grüfnisch zu Normal übersetzen')
    print('(c) Normal zu Grüfnisch Sprachausgabe')
    print('(d) Grüfnisch zu Normal Sprachausgabe')
    print('(x) Programm beenden')
    print()

    answer = input('Auswahl (a, b, c, d, x): ')
    selection = answer.lower().strip()
    if selection not in ['a', 'b', 'c', 'd', 'x']:
        print(f"!!! Selektierte Option '{selection}' nicht erkannt\n\n")
        return what_to_do()

    if selection == 'x':
        exit(0)

    text = input('Geben Sie einen Text ein: ')
    print()
    if selection == 'a':
        print(to_gruefnisch(text))
    elif selection == 'b':
        print(from_gruefnisch(text))
    elif selection == 'c':
        speak(to_gruefnisch(text))
    elif selection == 'd':
        speak(from_gruefnisch(text))
    print('\n--------------------------------\n')


while True:
    what_to_do()

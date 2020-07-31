from pyfiglet import Figlet, FigletFont
import inquirer


def prompt_font(font=None) -> str:
    questions = [
        inquirer.List(
            'font',
            message='Welche Schriftart soll benutzt werden?',
            choices=sorted(FigletFont.getFonts()),
            default=font,
            carousel=True
        )
    ]
    # answer: dict, e.g. {'font': 'isometric2'}
    answer = inquirer.prompt(questions)
    return answer['font']


questions = [
    inquirer.Text('text', message='Text', default='GBSL')
]

answer = inquirer.prompt(questions)
text = answer['text']

font = None

while True:
    font = prompt_font(font)
    figlet = Figlet(font=font)
    ascii_text = figlet.renderText(text)
    print(ascii_text)
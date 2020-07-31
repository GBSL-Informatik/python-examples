import cowsay
import inquirer


def prompt_character(character_name=None) -> str:
    questions = [
        inquirer.List(
            'character_name',
            message='Welcher Charakter soll sprechen?',
            choices=sorted(['beavis', 'cheese', 'daemon', 'cow', 'dragon', 'ghostbusters', 'kitty', 'meow', 'milk', 'stegosaurus', 'stimpy', 'turkey', 'turtle', 'tux']),
            default=character_name,
            carousel=True
        )
    ]
    # answer: dict, e.g. {'character': 'tux'}
    answer = inquirer.prompt(questions)
    return answer['character_name']


questions = [
    inquirer.Text('text', message='Text', default='GBSL')
]

answer = inquirer.prompt(questions)
text = answer['text']

character_name = None

while True:
    character_name = prompt_character(character_name)
    character = getattr(cowsay, character_name)
    ascii_text = character(text)
    print(ascii_text)
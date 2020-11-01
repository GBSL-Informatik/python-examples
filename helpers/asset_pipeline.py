from pathlib import Path
from typing import List, Union
import regex as re
# regex for "{{ filename }}" or "# {{ filename }}"
TEMPLATE_REGEX: re = re.compile(r'(?P<indent>[ \t]*?)(# *)?{{\s*(?P<file_name>[^=]*?)\s*}}')
# regex for "{{= key }}" or "# {{= key }}"
TEMPLATE_REPLACE_REGEX: re = re.compile(r'(?P<indent>[ \t]*?)(# *)?{{=\s*(?P<file_name>.*?)\s*}}')


def wrap_code(code: str, language: str = '', indent: str = ''):
    '''wraps code in markdown code block
    '''
    language = language.replace('.', '')
    return f'''```{language}
{code}
{indent}```'''


def indent_lines(lines: List[str], indent: str):
    lines = list(map(lambda line: f'{indent}{line.rstrip()}', lines))
    return '\n'.join(lines)


def get_file_path(file_dir: Path, file_name: str, lookup_folder: str = 'scripts') -> Union[Path, None]:
    if file_dir.joinpath(file_name).exists():
        return file_dir.joinpath(file_name)
    if file_dir.parts[-1] == lookup_folder:
        print('no script file found: ', file_dir.joinpath(file_name))
        return None
    return get_file_path(file_dir.joinpath(lookup_folder), file_name)


def process_template(template: str, values: dict = {}, lookup_dir: Path = Path(__file__).parent, lookup_folder: str = 'scripts'):
    place_holders = TEMPLATE_REGEX.findall(template)
    for match in place_holders:
        has_comment = len(match[1]) > 0
        file_name = match[2]
        script_file = get_file_path(lookup_dir, file_name, lookup_folder)
        if script_file is None:
            break

        with open(script_file, 'r') as f:
            script_lines = f.readlines()
        indent: str = match[0]
        raw_script = indent_lines(script_lines, indent)
        if has_comment:
            script = raw_script
        else:
            script = wrap_code(raw_script, language=script_file.suffix[1:], indent=indent)
        to_replace = re.compile(r'(# *)?{{\s*' + file_name + r'\s*}}')
        template = re.sub(to_replace, script, template)

    replacers = TEMPLATE_REPLACE_REGEX.findall(template)
    for match in replacers:
        key = match[2]
        indent: str = match[0]
        if key in values:
            val = str(values[key]).splitlines()
            if len(val) == 1:
                indent = ''
            script = indent_lines(val, indent)
            to_replace = re.compile(r'(# *)?{{=\s*' + key + r'\s*}}')
            template = re.sub(to_replace, script, template)
        else:
            print('No value found: ', key)
    return template


def process_file(file: Path, values: dict = {}, lookup_folder: str = 'scripts'):
    with open(file, 'r') as f:
        content = f.read()
    return process_template(content, values, file.parent, lookup_folder)


def process(root: Path, values: dict = {}):
    for file in root.rglob("*.py.*"):
        print(f"Process file: {file}")
        content = process_file(file, values)
        final_file = str(file).replace('.py.', '.')
        with open(final_file, 'w') as f:
            f.write(content)


if __name__ == '__main__':
    process(Path(__file__).parent)

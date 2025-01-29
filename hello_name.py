from pathlib import Path
name_path = Path('names.txt')
read_name = name_path.read_text()
if read_name:
    print(f'Hello, {read_name}')
else:
    name = input('Enter your name: ')
    name_path.write_text(name)
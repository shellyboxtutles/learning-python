from pathlib import Path
path = Path('vs_python_text_file_main_chat.txt')
messages = path.read_text().strip()
while True:
    print(messages)
    input1 = input("enter message: ")
    path.write_text(f"/n{input1} ")
    
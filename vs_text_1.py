from pathlib import Path
messages = Path('vs_python_text_file_main_chat.txt')
def update():
    counter = 1 
    while counter <=2:
        new_message = ''
        new_message = input(" ")
        new_message.write_text(new_message)

update()
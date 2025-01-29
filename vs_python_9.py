from pathlib import Path 
import json
import sys
try:
    import vs_python_acount_1
except ModuleNotFoundError:
    print("can't open file. \nfor help please contact 442-279-7552 or g.python.website.and.app.developers@gmail.com"), sys.exit()
try:
    path1 = Path('vs_python_text_file_main_chat.txt')
    var1 = path1.read_text()
except FileNotFoundError:
    path1 = json.dumps()
var1 = path1.read_text()
name = input("please enter your name: ")
while True:
    try:
        print(var1)
        input1 = input("")
        var1 += f"\n{name} wrote: \n{input1}"
        path1.write_text(var1)
    except UnicodeDecodeError:
        print("please only enter charecters. \ntry again.")
    except EOFError:
        print("please only enter charecters. \ntry again.")

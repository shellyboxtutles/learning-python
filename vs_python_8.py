from pathlib import Path
Path('vs_text_file_main_chat.txt')
input1 = input("please enter your name here: ")
print(f"hello {input1}")
input2 = input("please enter your zip code: ")
def enter_code():
    input3 = input("enter code: ")
    #if int(input3.strip) ==3464: print("okay")
    if int(input3) in Path: print("okay")
    else: print("sorry can't find that. \ntry again."), enter_code()

enter_code()
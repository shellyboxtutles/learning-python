import time
from pathlib import Path
password_path = Path('vs_python_txt_1.txt')
passwords = password_path.read_text()
update_path = passwords
password_dict = {}
password_pair = []
for user in passwords.splitlines():
    password_pair = user.split(':')
    password_dict[password_pair[0]] = password_pair[1]
counter1 = 1
def acces1():
    counter1 = 1
    while True:
        counter1 += 1
        if counter1 == 6: print("too many wrong answers. \nwait 30 minutes to try again"), time.sleep(1800)
        try:
            input2 = input("enter username: ")
            #if input2== f"{password_dict}": print("okay")
            if input2 in password_dict:
                input3 = input('enter password: ')
            else: 
                print("account does not exist. \ntry again.")
                continue
            if password_dict[str(input2)] == input3:
                print('access granted')
            else: 
                print("incorrect"), 
                continue
        except KeyError:
            pass


def create_acount():
    input2 = input('enter a username: ')
    input3 = input('enter a password: ')
    import vs_python_5
    password_dict[input2] = input3
    print('you are now logged in\n')
    update()

def update():
    new_passwords = ''
    for user in password_dict:
        new_passwords += f'{user}:{password_dict[user]}\n'
    password_path.write_text(new_passwords)
def back_door():
    input1 = input("enter secure acces pin: ")
    if input1 == str(8765): print("acces granted")
    else: print("wrong pin"), back_door()

def start():
    try:
        input1 = input('If you already have an existing acount write "login". If you do not have an existing acount, write "create acount". enter "programer" for secure programer acces. \nenter your answer here: ')
        if input1 =="login": acces1()
        elif input1 =="create acount": create_acount()
        elif input1 =="programer": back_door()
        else: print("sorry, could not get that. \ntry again"), start()
    except KeyboardInterrupt:
        print("sorry, could not get that. \ntry again"), start()
    except EOFError:
        print("sorry, could not get that. \ntry again"), start()
start()
access = ("allowed")
def login1():
    counter1 = 1
    password1 = True
    while password1:
        input1 = input("enter your password here: ")
        if input1 == "coco": password1 = False
        else: print("wrong password. try again.")
def login2():
    counter1 = 1
    password1 = True
    while password1:
        input1 = input("enter your password here: ")
        if input == "max": password2 = False
        else: print("wrong password. try again.")
input3 = input("enter your username here: ")
if input3 =="coco": login1()
if input3 =="shelly":login2()
else: print("can't find account")
print("access granted")
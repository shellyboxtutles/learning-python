import vs_python_acount_1
from random import randint
from random import choice
true1 = True
counter1 = 0
pikachu = 0
bulbasuar = 0 
charmander = 0
pokemon = ['pikachu', 'charmander', 'bulbasuar']
apeared = choice(pokemon)
name1 = f"{apeared}"
print(f"{apeared} apeared")
while true1 == True:
    input1 = input("catch? ")
    if input1 =="esc": exit
    else: print("...")
    var2 = randint(1, 10)
    print(var2)
    if var2 == 6: catch1 = "catch"
    elif var2 == 5: catch1 = "catch"
    elif var2 == 4: catch1 = "catch"
    elif var2 == 3: catch1 = "catch"
    elif var2 == 1: catch1 = "catch"
    elif var2 == 2: catch1 = "catch"
    else: catch1 = "escape", print("escaped")
    if catch1 =="catch": print(f"{name1} is in the poke ball...")
    if catch1 =="catch":  print("...")
    else: continue
    caught = 0
    random1 = randint(1, 2)
    print(random1)
    if catch1 =="catch":
        if random1 == 1:  
            if apeared =="pikachu": pikachu += 1
            elif apeared =="bulbasuar": bulbasuar += 1
            elif apeared =="charmander": charmander += 1
        else: print(f"{apeared} escaped the poke ball")
        if catch1 =="catch":
            if random1 == 1: true1 = False
            else: print(" ")
        else:print(" ")
    counter1 += 1
    if counter1 >= 5:
        print(f"{name1} ran away"), true1 == False
print(f"{bulbasuar} bulbasuar, {charmander} charmander, {pikachu} pikachu")
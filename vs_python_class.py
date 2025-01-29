class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")

    def ate_dinner(self):
        print(f"{self.name} ate our dinner")

name_1 = 'coco'
def doggy():
    blah_dog = Dog(name_1, 3)
    blah_dog.sit()
    blah_dog.roll_over()
    blah_dog.ate_dinner()

doggy()
name_1 = 'max'
doggy()
name_1 = input("enter you dogs name here: ")
doggy()
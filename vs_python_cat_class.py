class Cat:
    def __init__(self, age, breed, color, name):
        self.age = age
        self.breed = breed
        self.name = name
        self.color = color

    def get_info(self):
        print(f"{self.name} {self.breed} {self.color} {self.age}")

cat1 = Cat('3 months old', 'siberian', 'red point', 'andrei')
cat1.get_info()
def get_cat_info():
    input1 = input("enter age: ")
    input2 = input("enter breed: ")
    input3 = input("enter color: ")
    input4 = input("enter name: ")
    cat2 = f"{input4} {input2} {input3} {input1}"    
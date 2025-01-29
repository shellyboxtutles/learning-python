class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 138591
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: print("you can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_car = Car('honda', 'odyssey', 2019)
print(my_car.get_descriptive_name())

my_car.update_odometer(23500)
my_car.read_odometer()

my_car.increment_odometer(100)
my_car.read_odometer()

my_car.odometer_reading = (23)
my_car.read_odometer()

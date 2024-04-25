
#Setting a default value
class Car:
    "A simple method of creating a car class to demonstrate default value"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.milage = 0


#3 ways to modify attribute values
# change the value directly through an isinstance
# set the value through a method
# increment the value(add a certain amount to it) through a model

#1
my_car = Car("Toyota", "Highlander", "2020")
my_car.milage = 23
print(my_car.milage)

#2
class Car:
    "A simple method of creating a car class to demonstrate default value"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.milage = 0

    def update_milage(self, milage):
        self.milage = milage

#3
class Car:
    "A simple method of creating a car class to demonstrate default value"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.milage = 0

    def update_milage(self, milage):
        self.milage += milage
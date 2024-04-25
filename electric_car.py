class Car:
    "A simple method of creating a car class to demonstrate default value"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.milage = 0

    def update_milage(self, milage):
        self.milage += milage

class ElectricCar(Car):
    "A method of creating a child class using Car as the parent class"

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
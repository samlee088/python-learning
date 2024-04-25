class Car:
    "A simple method of creating a car class to demonstrate default value"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.milage = 0

    def update_milage(self, milage):
        self.milage += milage

    def print_car_information(self):
        print(f"car information: {self.make}, {self.model}, {self.year}")

class ElectricCar(Car):
    "A method of creating a child class using Car as the parent class"

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.batterySize = 20
    
    def print_battery_information(self): 
        """Prints out information about the car's battery"""
        print(f"Battery size is: {self.batterySize}")
    

my_electric_car = ElectricCar("Toyota","Highlander","2020")
my_electric_car.print_car_information()
my_electric_car.print_battery_information()
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

    #Example of a child being able to override the parent class function
    def update_milage(self):
        """Electric car update is not available"""
        print(f"Unable to update milage for electric car type")
    

my_electric_car = ElectricCar("Toyota","Highlander","2020")
my_electric_car.print_car_information()
my_electric_car.print_battery_information()
my_electric_car.update_milage()


#Composition example
class ElectricCar(Car):
    "A method of creating a child class using Car as the parent class"

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def print_battery_information(self): 
        """Prints out information about the car's battery"""
        print(f"Battery size is: {self.batterySize}")

    #Example of a child being able to override the parent class function
    def update_milage(self):
        """Electric car update is not available"""
        print(f"Unable to update milage for electric car type")

class Battery:
    def __init__(self, battery_size = 40):
        """A separate class to distinguish batter for electricCar class"""
        self.battery = battery_size

    def describe_battery_size(self):
        """A method to describe the battery size"""
        print(f"Battery Size: {self.battery}")
    

my_battery_electric_car = ElectricCar("Toyota", "Camry", "2010")
my_battery_electric_car.battery.describe_battery_size()


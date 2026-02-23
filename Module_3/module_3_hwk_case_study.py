'''
module_3_hwk_case_study.py

Steve Kepler
SDEV220
22 February 2026
Case Study: Functions and Classes


'''

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def  __init__(self):
        self.vehicle_type = "car"
        self.year = input("Input model year: ")
        self.make = input("input make: ")
        self.model = input("Input model: ")
        while (doors := input("Input number of doors: ")) not in ('2', '4'):
            print("Please enter either 2 or 4.")
        self.doors = doors
        roof = input("Enter whether it has a sun roof (Y/N):")
        if roof.upper() == 'Y':
            self.roof = 'sun roof'
        else:
            self.roof = 'solid'
        print(self)


    def __str__(self):
        return (
        f"Vehicle type: {self.vehicle_type}\n"
        f"Make: {self.make}\n"
        f"Model: {self.model}\n"
        f"Number of doors: {self.doors}\n"
        f"Type of roof: {self.roof}"
        )
    
my_car = Automobile()
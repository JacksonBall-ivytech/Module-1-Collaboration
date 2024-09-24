class Vehicle:
    def __init__(self, vehicle_type):
        self.type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
    def describe_car(self):
        details = (
            f'Vehicle type: {self.type}\n'
            f'Year: {self.year}\n'
            f'Make: {self.make}\n'
            f'Model: {self.model}\n'
            f'Number of doors: {self.doors}\n'
            f'Type of roof: {self.roof}\n'
        )
        print(details)

vehicle_type = input('What kind of vehicle do you have?: ')

if vehicle_type.lower() in ['car', 'automobile', 'motorcar', 'auto']:
    year = input('What year is your car?: ')
    make = input('What is the make of your car?: ')
    model = input('What is the model of your car?: ')
    doors = input('How many doors does it have?: ')
    roof = input('What type of roof does it have?: ')
    car = Automobile(vehicle_type, year, make, model, doors, roof)
else:
    vehicle = Vehicle(vehicle_type)
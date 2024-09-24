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
        print(f'Vehicle type: {self.type}')
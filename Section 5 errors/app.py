class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car): #if car is not an instance of Car class
            raise TypeError(f"Tried to add {car.__class__.__name__} to the garage, but can only add Car objects")
        #raise NotImplementedError('WIP lol')
        self.cars.append(car)

ford = Garage()
car = Car('Fiest', 'a')
try:
    ford.add_car(car)
except TypeError:
    print('Your car was not a car')

#ford.add_car('Furry')

#Task below
"""
for the function below, add your code in appropriate place that checks the input n.
n should be a non-negative integer, otherwise a ValueError should be raised
and a proper error message should be provided informing the user of the error
for simplicity, you may assume that the input is always an integer for this exercise
"""
def count_from_zero_to_n(n):
    if n<0 or n.type != int:
        raise ValueError("N should be positive integer")
    for x in range(0, n+1):
        print(x)
count_from_zero_to_n(-1.1)
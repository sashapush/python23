from abc import ABCMeta, abstractmethod
# abc means abstract base class
class Animal(metaclass=ABCMeta):
    def walk(self):
        print("Walking...")

    @abstractmethod  # it's not a specific animal method, so it's a responsibility of child classes to implement that method
    def num_legs(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 4


class Monkey(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):  # it's possible to inherit method with 4 legs from Animal, and override it to 2
        # but THIS method has to be in child class or this child class object can't be created
        return 2


class Whale:
    def __init__(self, name):
        self.name

    def num_legs(self):
        return 0


# a = Animal()
# print(a.num_legs())
d = Dog("Sam")
print(d.num_legs())

animals = [Dog("Ass"), Monkey("Sammy")]
for a in animals:
    print(isinstance(a, Animal)) #to check if a is an instance of Animal class)
    print(a.num_legs()) #returns 4 and 2

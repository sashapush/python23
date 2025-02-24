"""
modify the Animal class so that:
- The `Animal` class can no longer be instantiated.
- Any subclass of `Animal` class must have a `get_favourite_food()` method
    so that the `hungry()` method can remain consistent.
remember to import proper packages here
"""
from abc import ABCMeta, abstractmethod
# modify the Animal class
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def get_favourite_food(self):
        pass

    def hungry(self):
        print('I want to eat {}!'.format(self.get_favourite_food()))


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    @classmethod
    def get_favourite_food(cls):
        return 'ribs'


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    @classmethod
    def get_favourite_food(cls):
        return 'meat'
doge = Dog("doge")
doge.hungry()
cat = Cat("meow")
cat.hungry()
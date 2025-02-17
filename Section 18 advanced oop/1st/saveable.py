from abc import ABCMeta, abstractmethod
from database import Database
class Saveable(metaclass=ABCMeta): #superclass with abstract methods. In another programming langs it's called an interface because it defines functionality which should be in subclass
    #you can't instantiate interface.
    def save(self):
        Database.insert(self.to_dict())

    @abstractmethod  # it's not a specific  method, so it's a responsibility of child classes to implement that method
    def to_dict(self):
        pass
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclass"""
        pass

class Dog(Animal):
    """txt"""
    def sound(self):
        return ("Bark")
    
class Cat(Animal):
    """txt"""
    def sound(self):
        return ("Meow")

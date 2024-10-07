#!/usr/bin/python3
"""
Metodo
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Clase Animal que hereda de ABC y define un metodo Sound
    """
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """
    Clase Dog que hereda de Animal y que hereda el metodo Sound
    """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """
    Clase Cat que hereda de Animal y que hereda el metodo Sound
    """
    def sound(self):
        return "Meow"

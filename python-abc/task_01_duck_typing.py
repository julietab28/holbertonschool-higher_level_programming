#!/usr/bin/python3
"""
Modulo de clase Shape
"""
from abc import ABC, abstractmethod
from math import math


class Shape(ABC):
    """
    Clase Shape
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """
    Clase que define un Square con herencia de Shape
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * self.radius * pi

class Rectangle(Shape):
    """
    Clase que define un Rectangle que heredea de Shape
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)

def shape_info(shape):
    """
    Duck typing
    """
    area = shape.area()
    perimeter = shape.perimeter()
    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))

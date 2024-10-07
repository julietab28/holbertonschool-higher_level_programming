#!/usr/bin/python3
"""
Modulo de una clase
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Clase que hereda de BaseGeometry, representa un rectangulo
    """
    def __init__(self, width, height):
        """
        Inicializamos valores
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

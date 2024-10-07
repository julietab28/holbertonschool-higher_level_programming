#!/usr/bin/python3
"""
Modulo de una clase Square que respresenta un cuadrado
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Clase que hereda de Rectangle, representa un Cuadrado
    """
    def __init__(self, size):
        """
        Inicializmos los valores dependiendo de si size es un integer o no
        """
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """
        Clacular area
        """
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

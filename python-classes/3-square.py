#!/usr/bin/python3
"""
Este modulo crea una clase Square que representa un cuadrado
"""


class Square:
    """
    Clase que representa un cuadrado

    Atributos:
        __size (int): Tamaño del cuadrado. Debe ser un entero no negativo

    Métodos:
        __init__(self, size=0): Inicializa una instancia de la clase Square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")

        self.__size = size
    def area(size):
        sq_area = size * size
        return sq_area
#!/usr/bin/python3
"""
Este modulo crea una clase Square que representa un cuadrado
"""


class Square:
    """
    Clase que representa a un cuadrado
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """
        Getter: nos permite acceder a size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter: permite modificar el atributo, lo uso para poder asignarle un
        nuevo valor a size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            array = []
            for _ in range('#' * self.__size):
                array.append(self.__size)

            sq = '\n'.join(array)
            return sq

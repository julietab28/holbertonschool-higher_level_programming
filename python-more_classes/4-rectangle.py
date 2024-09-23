#!/usr/bin/python3
"""
Creacion de una clase Rectangulo que representa un rectangulo
"""


class Rectangle:
    """
    Clase que representa un rectangulo
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter. Permite modificar el atributo,
        le asignamos un nuevo valor a width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter. Permite modificar el atributo,
        le asignamos un nuevo valor a height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height <= 0 or self.__width <= 0:
            return 0
        else:
            return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join('#' * self.__width for _ in range(self.__height))
    def __repr__(self):
        rect = "\n".join('#' * self.__width for _ in range(self.__height))
        return rect

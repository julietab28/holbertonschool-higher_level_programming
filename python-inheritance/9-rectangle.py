#!/usr/bin/python3
"""
Modulo de una clase
"""


class BaseGeometry:
    """
    Clase que representa geometria
    """
    def area(self):
        """
        Metodo de area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valida si el value es de tipo integer y si es mayor que 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    Clase que hereda de BaseGeometry, representa un rectangulo
    """
    def __init__(self, width, height):
        """
        Inicializamos valores
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calcula el area de un rectangulo
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Restorna un mensaje con la descripcion del rectangulo
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

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

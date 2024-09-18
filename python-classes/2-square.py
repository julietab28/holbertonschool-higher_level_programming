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
        is_int(self): Valida si el tamaño es un entero no negativo
    """

    def __init__(self, size=0):
        """
        Inicializa un nuevo objeto Square con el tamaño especificado

        Args:
            size (int): El tamaño del lado del cuadrado. Por defecto es 0
        
        Raises:
            ValueError: Si size no es un entero o es menor que 0
        """
        self.__size = size

    def is_int(self):
        """
        Verifica si el tamaño del cuadrado es un entero no negativo

        Raises:
            ValueError: Si el tamaño no es un entero o es menor que 0
        """
        if isinstance(self.size, int):
            if self.size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

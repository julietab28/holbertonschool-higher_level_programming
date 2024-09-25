#!/usr/bin/python3
"""
is_same_class
"""


    def is_same_class(obj, a_class):
        """
        Verifica si un objeto es exactamente de la clase especificada

        Args:
            obj: El objeto a verificar
            a_class: La clase con la que se desea comparar el objeto

        Returns:
            bool: True si 'obj' es una instancia de 'a_class', False en caso contrario
        """
        return isinstance(obj, a_class)

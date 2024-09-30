#!/usr/bin/python3
"""
Módulo que define la función is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
    Verifica si un objeto es una instancia de una clase o
    de una subclase.

    Args:
        obj: El objeto a verificar.
        a_class: La clase con la que se desea comparar el objeto.

    Returns:
        bool: True si 'obj' es una instancia de 'a_class' o de
        una subclase de 'a_class', False en caso contrario.
    """
    return isinstance(obj, a_class)

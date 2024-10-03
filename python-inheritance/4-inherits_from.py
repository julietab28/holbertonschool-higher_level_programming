#!/usr/bin/python3
"""
Módulo que define la función is_kind_of_class.
"""


def inherits_from(obj, a_class):
    """
    Verifica si un objeto es una instancia de una
    clase que heredó (directa o indirectamente)
    de una clase especificada.

    Parámetros:
    obj: Cualquiera
        El objeto que se va a verificar.
    a_class: type
        La clase contra la cual se va a verificar.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

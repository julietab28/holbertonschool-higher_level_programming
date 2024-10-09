#!/usr/bin/python3
"""
Modulo
"""


def append_write(filename="", text=""):
    """
    Funcion que agrega una cadena de texto
    al final de un archivo
    """
    with open(filename, 'a', encoding="utf-8") as f:
        file = f.write()
        return len(text)

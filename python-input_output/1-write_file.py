#!/usr/bin/python3
"""
Modulo 2
"""


def write_file(filename="", text=""):
    """
    Funcion que escribe dentro de un archivo un
    texto, y luego retorna el numero de
    caracteres del texto
    """
    with open(filename, 'w', encoding="utf-8") as f:
        file = f.write(text)
        return len(text)

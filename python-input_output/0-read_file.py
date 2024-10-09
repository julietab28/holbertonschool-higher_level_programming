#!/usr/bin/python3
"""
Modulo
"""


def read_file(filename=""):
    """
    Funcion que lee un archivo y luego lo imprime
    """
    with open(filename, 'r', encoding="utf-8") as f:
        file = f.read()
        print("{}".format(file))

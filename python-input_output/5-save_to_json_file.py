#!/usr/bin/python3
"""
Modulo 5
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Funcion que escribe un objeto dentro de un archivo
    """
    with open(filename, 'w', encoding="utf-8") as f:
        file = f.write(my_obj)

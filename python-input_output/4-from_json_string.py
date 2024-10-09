#!/usr/bin/python3
"""
Modulo 5
"""
import json


def from_json_string(my_str):
    """
    Funcion que convierte un string JSON
    a un objeto de Python
    """
    x = json.loads(my_str)
    return x

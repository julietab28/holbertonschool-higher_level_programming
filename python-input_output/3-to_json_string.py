#!/usr/bin/python3
"""
Modulo 3
"""
import json


def to_json_string(my_obj):
    """
    Funcion que retorna la representacion de un objeto JSON
    """
    with open(my_obj, 'r', encoding="utf-8") as x:
        x = json.dumps(my_obj)
        return x

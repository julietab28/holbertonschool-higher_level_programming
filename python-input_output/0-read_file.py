#!/usr/bin/python3
"""
Modulo
"""


def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as f:
        file = f.read()
        print("{}".format(file))

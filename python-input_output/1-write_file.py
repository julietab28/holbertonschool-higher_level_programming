#!/usr/bin/python3
"""
Modulo 2
"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as f:
        file = f.write(text)
        return len(text)

#!/usr/bin/env python3
def uppercase(str):
    palabra = ""
    for letter in str:
        if ord(letter) >= 65 and ord(letter) <= 90:
            palabra += letter
        elif ord(letter) == 32:
            palabra += letter    
        else:
            palabra += chr(ord(letter) - 32)
    return palabra

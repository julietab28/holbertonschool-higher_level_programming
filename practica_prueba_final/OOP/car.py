#!/usr/bin/python3

class Car():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        dict = {
            "brand": self.brand,
            "model": self.model,
            "year": self.year
        }
        print(dict)
    

autito = Car("bmw", "lol", "2026")
autito.display_info()
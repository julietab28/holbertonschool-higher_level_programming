#!/usr/bin/python3

class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        super().__init__
    
    def make_sound(self):
        print("Woof")

animal = Animal("pepe", "dog")
perro = Dog("pepin", "dog") 

animal.make_sound()
perro.make_sound()
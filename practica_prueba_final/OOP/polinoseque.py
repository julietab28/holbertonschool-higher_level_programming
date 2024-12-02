#!/usr/bin/python3

class Shape():
    def area(self):
        raise NotImplementedError("lol")

class Circle(Shape):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return 3.14 * self.radio * self.radio

class Rectangle(Shape):
    def __init__(self, leng, wid):
        self.leng = leng
        self.wid = wid
    def area(self):
        return self.leng * self.wid
    
def areas(shape):
    print("Area:", shape.area())


circle = Circle(12)
rect = Rectangle(13, 14)

areas(circle)
areas(rect)
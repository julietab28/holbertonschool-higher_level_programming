#!/usr/bin/python3
"""
Mtodo de clase
"""


class CountedIterator:
    def __init__(self, i):
        self.iterator = iter(i)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        item = next(self.iterator)
        self.counter += 1
        return item

#!/usr/bin/python3
"""
Modulo de clase Shape
"""


class VerboseList(list):
    """
    Clase 
    """
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, item):
        item_popped = super.pop(item)
        print("Popped [{}] from the list.".format(item_popped))

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if idx < 0:
        return my_list
    elif idx > (len(my_list) - 1):
        return my_list
    else:
        for x in range(0, len(my_list)):
            if x == idx:
                new_list[x] = element
        return new_list

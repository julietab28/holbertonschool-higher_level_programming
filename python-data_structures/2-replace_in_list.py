#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    new_list = []
    if idx < 0:
        return my_list
    elif idx > (len(my_list) - 1):
        return my_list
    else:
        new_list = my_list
        new_list[idx] = element
        return new_list

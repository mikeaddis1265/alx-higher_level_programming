#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return "None"
    max = my_list[0]
    for i in range(length - 1):
        if my_list[i] > max:
            max = my_list[i]
    return max

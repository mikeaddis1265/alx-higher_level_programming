#!/usr/bin/python3
def no_c(my_string):
    temp = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            temp += i
    return temp

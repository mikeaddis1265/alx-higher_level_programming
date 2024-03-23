#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_list = sorted(a_dictionary)
    for i in key_list:
        print("{}: {}".format(i, a_dictionary[i]))

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length1 = len(tuple_a)
    length2 = len(tuple_b)

    if length1 == 0:
        a1 = 0
        a2 = 0
    elif length2 == 1:
        a1 = tuple_a[0]
        a2 = 0
    else:
        a1 = tuple_a[0]
        a2 = tuple_b[1]

    if length2 == 0:
        b1 = 0
        b2 = 0
    elif length2 == 1:
        b1 = tuple_b[0]
        b2 = 0
    else:
        b1 = tuple_b[0]
        b2 = tuple_b[1]
    new_tuple = (a1 + a2, b1 + b2)
    return (new_tuple)

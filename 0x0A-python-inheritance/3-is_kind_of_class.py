#!/usr/bin/pyhton3
"""returns True if the object is an instance of, or if the object is an instance of a class that inherited from;
otherwise False
"""


def is_kind_of_class(obj, a_class):
    """returns true if an object is an instance of the class or inherited class"""
    return isinstance(obj, a_class)

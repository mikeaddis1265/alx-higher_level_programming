#!usr/bin/python3
def is_same_class(obj, a_class):
    """if  an object is exactly an instance of the specified class
            return true
        else
            return false
    """
    return type(obj) == a_class

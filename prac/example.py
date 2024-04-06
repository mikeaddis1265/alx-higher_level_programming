def add(x, y):
    """add function"""
    return x + y

def sub(x, y):
    """subtraction function"""
    return x - y

def mul(x, y):
    """multiplication function"""
    return x * y

def div(x, y):
    """add function"""
    if y == 0:
        raise ValueError("can not divice by zero")
    return x // y

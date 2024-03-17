import dis

def myfunc():
    x = 42
    return x * 2

dis.show_code(myfunc)

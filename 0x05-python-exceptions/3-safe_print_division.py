def safe_print_division(a, b):
    try:
        print("{} / {} = {}" .format(a, b, a / b))
    except ZeroDivisionError:
        print("{} / {} = {}" .format(a, b, None))
def add_integer(a, b=98):
    """
    Adds two integers, with the option to specify a default value for the second integer.

    Parameters:
    - a (int or float): The first integer to add. If a float, it will be converted to an integer.
    - b (int or float, optional): The second integer to add. Defaults to 98. If a float, it will be converted to an integer.

    Returns:
    - int: The sum of a and b.

    Raises:
    - TypeError: If a or b is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    
    return a + b

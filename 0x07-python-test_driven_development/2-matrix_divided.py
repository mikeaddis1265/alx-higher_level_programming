def matrix_divided(matrix, div):
    """
    a function that divides all elements of a matrix.

    parameters:
    - matrix : a list of lists containing integers or floats.
    - div : must be a float or int

    Returns:
    - Returns a new matrix, by dividing the argument matrix by div rounded to 2 decimal places

    Raises:
    - TypeError: if any element in the matrix is not int or float
    - ZeroDivisionError: if the passed argument div is zero
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if div is None:
        return matrix

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0]) if matrix else 0
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    result_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return result_matrix

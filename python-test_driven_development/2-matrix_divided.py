#!/usr/bin/python3
"""
This module contains a function for divivding a matrix
"""


def matrix_divided(matrix, div):
    """
    Creates a new matrix the elements of which are the elements of given matrix
    divided by two
    
    Args:
        matrix (list): given matrix
        div (int or float): number by which elements will be divided
        
    Return:
        new_matrix (list): matrix with elements of given matrix divided my div
        
    Raises:
        TypeError: if div and elements of matrix are not an int or float, the lengthes
        of rows in matrix are not equal
        
        ZeroDivisionError: if div == 0
    """
    row_length = len(matrix[0])
    new_matrix = []
    if (type(div) is not int and type(div) is not float):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if (len(row) != row_length):
            raise TypeError("matrix must have each row with the same size")
        new_row = []
        for el in row:
            if (type(el) is not int and type(el) is not float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            new_row.append(round(el / div, 2))

        new_matrix.append(new_row)

    return (new_matrix)

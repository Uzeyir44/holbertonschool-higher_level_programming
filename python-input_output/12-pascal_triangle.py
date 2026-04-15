#!/usr/bin/python3
"""
This module contains pascal_triangle function
"""


def pascal_triangle(n):
    """
    This functian creates a pascal triangle

    Args:
        n (int): the height of triangle

    Return:
        ls (list): a list which contains other lists
        which represent the levels of pascal triangle
    """
    ls = []
    for i in range(n):
        if (i == 0):
            ls.append([1])
            continue

        tmp_ls = ["" for _ in range(i+1)]
        tmp_ls[0] = 1
        tmp_ls[i] = 1

        for j in range(i-1):
            tmp_ls[j+1] = (ls[i-1][j] + ls[i-1][j+1])

        ls.append(tmp_ls)
    return (ls)

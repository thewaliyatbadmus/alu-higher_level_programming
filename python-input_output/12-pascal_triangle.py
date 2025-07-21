#!/usr/bin/python3
"""
Module defines pascal_triangle function.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n.

    Args:
        n (int): Number of rows.

    Returns:
        list: Pascal's triangle as a list of lists.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        if i == 0:
            row = [1]
        else:
            prev_row = triangle[i - 1]
            row = [1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)
        triangle.append(row)

    return triangle

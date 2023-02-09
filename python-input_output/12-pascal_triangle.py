#!/usr/bin/python3
"""Function pascal triangle"""


def pascal_triangle(n):
    """function for the triangle"""

    a = []
    b = []
    if n <= 0:
        return []
    for i in range(n):
        if i == 0:
            a.append([1])
        else:
            b = [1]
        for j in range(1, i):
            b.append(a[i - 1][j - 1] + a[i - 1][j])
            b.append(1)
            a.append(b)
    return a

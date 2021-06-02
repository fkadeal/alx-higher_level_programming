#!/bin/user/python3

def pascal_triangle(n):
     """
    Create a function def pascal_triangle(n):
    that returns a list of lists of integers representing
    the Pascals triangle of n
    """
    
    if n <= 0:
        return []
    temp = []
    l = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if i == 0 or j == 0 or i == j:
                row.append(1)
            else:
                row.append(l[j] + l[j - 1])
        l = row
        temp.append(row)
    return temp

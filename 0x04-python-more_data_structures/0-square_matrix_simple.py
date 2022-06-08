#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []

    for i in matrix:
        newmatrix.append(list(map(lambda x: x ** 2, i)))
    return newmatrix

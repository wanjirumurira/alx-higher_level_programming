#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    square = [[i*i for i in j] for j in new_matrix]
    return square

#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda x: list((x[0] ** 2, x[1] ** 2, x[2] ** 2)), matrix))

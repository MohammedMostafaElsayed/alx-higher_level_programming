#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq = []
    sqm = []
    for i in matrix:
        for j in i:
            sq.append(j * j)
        sqm.append(sq)
        sq = []
    return sqm

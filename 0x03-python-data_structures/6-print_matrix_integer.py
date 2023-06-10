#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = 0
    for i in matrix:
        x = 0
        for j in i:
            if x == len(i) - 1:
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
            x += 1
        print("")

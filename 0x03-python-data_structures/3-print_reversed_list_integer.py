#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n_list = my_list[::-1]
    for i in n_list:
        print("{:d}".format(i))

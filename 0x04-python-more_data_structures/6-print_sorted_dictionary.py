#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    k = list(a_dictionary.keys())
    v = list(a_dictionary.values())
    x = map((lambda q, z: "{}: {}".format(q, z)), k, v)
    for i in x:
        print(i)

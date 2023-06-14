#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    k = list(a_dictionary.items())
    k.sort()
    d = dict(k)
    k = list(d.keys())
    v = list(d.values())
    x = map((lambda q, z: "{}: {}".format(q, z)), k, v)
    for i in x:
        print(i)

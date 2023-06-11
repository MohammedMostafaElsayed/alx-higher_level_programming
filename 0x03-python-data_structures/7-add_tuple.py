#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    xx = []
    w = list(tuple_b)
    z = list(tuple_a)
    for j in range(0, 2):
        if len(tuple_b) < 2:
            w.append(0)
        if len(tuple_a) < 2:
            z.append(0)
    for i in range(0, 2):
        x.append(z[i] + w[i])
    return tuple(x)

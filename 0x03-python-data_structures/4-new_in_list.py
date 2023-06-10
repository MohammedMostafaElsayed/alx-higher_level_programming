#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n_list = my_list[::]
    if idx < 0:
        return n_list
    elif idx > len(n_list) - 1:
        return n_list
    else:
        n_list[idx] = element
        return n_list

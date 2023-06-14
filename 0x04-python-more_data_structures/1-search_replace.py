#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    for i in range(1, len(new)):
        if new[i] == search:
            new[i] = replace
    return new

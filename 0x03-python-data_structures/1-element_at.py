#!/usr/bin/python3
def element_at(my_list, idx):
    n = 0
    for i in my_list:
        if idx == n:
            return i
        n += 1

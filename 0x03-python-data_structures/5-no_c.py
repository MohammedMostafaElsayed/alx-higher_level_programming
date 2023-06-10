#!/usr/bin/python3
def no_c(my_string):
    s = ""
    for i in my_string:
        if ord(i) == ord('c') or ord(i) == ord('C'):
            continue
        s += i
    return s

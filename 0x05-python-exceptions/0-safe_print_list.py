#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    z = 0
    try:
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end="")
            z = z + 1
    except TypeError:
        pass
    finally:
        print("")
        return z

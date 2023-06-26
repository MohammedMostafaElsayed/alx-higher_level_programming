#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    z = 0
    try:
        for i in range(0, x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                z = z + 1
    except TypeError:
        pass
    finally:
        print("")
        return z

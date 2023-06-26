#!/usr/bin/python3
def safe_print_integer(value):
    x = False
    try:
        print("{:d}".format(value))
        x = True
    except TypeError:
        pass
    finally:
        return x

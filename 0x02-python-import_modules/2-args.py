#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    n = len(argv)
    if n == 1:
        print("0 arguments.")
    else:
        print("{:d} arguments:".format(n - 1))
        for i in range(1, n):
            print("{:d}: {:s}".format(i, argv[i]))

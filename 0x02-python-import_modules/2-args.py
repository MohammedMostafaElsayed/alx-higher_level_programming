#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    n = len(argv) - 1
    if n == 0:
        print("{:d} arguments.".format(n))
    elif n == 1:
        print("{:d} argument:\n{:d}: {:s}".format(n, n, argv[n]))
    else:
        print("{:d} arguments:".format(n))
        for i in range(1, n + 1):
            print("{:d}: {:s}".format(i, argv[i]))

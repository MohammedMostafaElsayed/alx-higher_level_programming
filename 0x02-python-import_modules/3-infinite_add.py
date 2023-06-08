#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    n = len(argv)
    su = 0
    for i in range(1, n):
        su += int(argv[i])
    print(su)

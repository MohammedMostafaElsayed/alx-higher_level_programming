#!/usr/bin/python3
def uppercase(str):
    rs = ""
    for i in str:
        if (ord(i) >= ord('a') and ord(i) <= ord('z')):
            rs += chr(ord(i) - 32)
        else:
            rs += i
    print("{:s}".format(rs))

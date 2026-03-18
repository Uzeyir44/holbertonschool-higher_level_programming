#!/usr/bin/python3
def uppercase(str):
    new = ""
    for i in str:
        if ("a" <= i <= "z"):
            new += chr(ord(i) - 32)
        else:
            new += i

    print("{}".format(new))

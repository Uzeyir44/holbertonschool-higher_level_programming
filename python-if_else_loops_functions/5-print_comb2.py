#!/usr/bin/python3
for i in range(100):
    if (i != 0):
        print(", ", end="")
    else:
        print("{:02}".format(i))

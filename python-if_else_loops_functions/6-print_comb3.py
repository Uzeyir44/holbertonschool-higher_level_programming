#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if (i != 0):
            print(", ", end="")
        
        if (i != 8 or j != 9):
            print("{:02}".format(i*10 + j), end="")
        else:
            print("{:02}".format(i*10 + j))

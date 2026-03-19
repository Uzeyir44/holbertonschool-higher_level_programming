#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))

a = [1, 2, 3]
print_reversed_list_integer(a)
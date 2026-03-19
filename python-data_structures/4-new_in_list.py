#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if (idx <= -1 or idx >= len(my_list)):
        return (my_list)

    a = my_list[:]
    a[idx] = element
    return (a)

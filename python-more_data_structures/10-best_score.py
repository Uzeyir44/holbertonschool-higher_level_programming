#!/usr/bin/python3

def best_score(a_dictionary):
    if (a_dictionary is None or len(a_dictionary) == 0):
        return (None)

    answ = max(a_dictionary.values())

    for k in a_dictionary:
        if (a_dictionary[k] == answ):
            return (k)

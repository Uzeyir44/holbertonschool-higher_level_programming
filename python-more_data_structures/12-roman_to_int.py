#!/usr/bin/python3

def roman_to_int(roman_string):
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    answ = 0

    if (type(roman_string) is not str or roman_string is None):
        return (0)

    for i in range(len(roman_string)):
        if (i != len(roman_string) - 1):
            if (rom[roman_string[i]] < rom[roman_string[i + 1]]):
                answ -= rom[roman_string[i]]
            else:
                answ += rom[roman_string[i]]
        else:
            answ += rom[roman_string[i]]

    return (answ)

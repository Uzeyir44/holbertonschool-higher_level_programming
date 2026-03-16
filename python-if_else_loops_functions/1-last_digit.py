#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l = number % 10

print(f"Last digit of {number} is ", end = "")

if (l == 0):
    print(f"{l} and is 0")
elif (l < 6):
    print(f"{l} and is less than 6 and not 0")
else:
    print(f"{l} and is greater than 5")

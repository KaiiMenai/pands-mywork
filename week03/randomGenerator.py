# randomGenerator.py
# This program will print out a random number between 1 and 10.
# author: Kyra Menai Hamilton

import random
print("Please state a start and end for range.")
start = int(input("Enter start number: "))
stop = int(input("Enter end number: "))

number = random.randint(start, stop)
print("Here is a random number, {}.".format(number))

# Reference:
# Using randint() function: https://www.geeksforgeeks.org/python-generate-random-numbers-within-a-given-range-and-store-in-a-list/
# Can also state if the output value needs to be above/below a specific value.

# More info on random module work here: https://www.w3schools.com/Python/module_random.asp

# END
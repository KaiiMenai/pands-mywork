# floor.py
# This program will read in a float and outputs an integer that is rounded down.
# Do NOT use if accuracy is necessary.
# author: Kyra Menai Hamilton

import math

numbertofloor = float(input("Enter a float number:"))
floorednumber = math.floor(numbertofloor)
print('{} floored is {}.'.format(numbertofloor, floorednumber))

# Inputting a number like 8.8 will give an output of 8.
# Output:
    # Enter a float number:8.8 
    # 8.8 floored is 8.

# END
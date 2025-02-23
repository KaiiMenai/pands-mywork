# round.py
# This program reads in a number and outputs it rounded to the nearest EVEN number.
# That is, the program takes in a float and outputs an integer, either rounded up or down.
# author: Kyra Menai Hamilton

# Note: This program rounds to the nearest EVEN number, so do not use if accuracy is required.
# i.e. 4.5 will round to 4, 7.5 will round to 8.

numberToRound = float(input("Enter a float number:"))
roundedNumber = round(numberToRound)
print ( '{} rounded is {}.'.format(numberToRound,roundedNumber))

# Inputting a number such as 6.9 will round to 7.
# For example:
    # Enter a float number:6.9
    # 6.9 rounded is 7.

# END
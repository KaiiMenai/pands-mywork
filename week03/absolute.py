# absolute.py
# This program reads in a number and outputs the absolute value of that number. 
# That is, the program takes in a number and gives its absolute value (ie -4 or 4 would both give an output of 4).
# author: Kyra Menai Hamilton

# The inpput will be read as a string (str()), so it needs to be input as a float in order to do the abs() function as this is a mathematical function. 

number = float(input("Enter a number: "))
absoluteValue = abs(number)
print('The absolute value of {} is {}.'.format(number, absoluteValue))


# Inputting a number such as -7 will give an output of 7.
    # Enter a number: -7
    # The absolute value of -7.0 is 7.0.

# Inputting a number such as 7 will give an output of 7.
    # Enter a number: 7
    # The absolute value of 7.0 is 7.0.

# Inputting a number such as 6.9 will give an output of 6.9.
    # Enter a number: 6.9
    # The absolute value of 6.9 is 6.9.

# Full stop added to the print() function to tidy up the output.
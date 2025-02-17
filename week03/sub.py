# sub.py
# This program reads in two numbers, and subtracts the second one from the first one.
# author: Kyra Menai Hamilton

# The input reads in a string so it needs to be converted it into an int() to be able to perform mathematical operations.

x = int(input("Enter first number: "))   # The input will return a string so the int() is used to convert it to an integer.
y = int(input("Enter second number: "))
answer= x-y
print("{} minus {} is {} ".format(x, y, answer))

# To tidy up the answer and add correct grammar - print("{} minus {} is {}.".format(x, y, answer))
# If something like 'hello' is entered it will give an error. 

# Like:
# Enter first number: 40
# Enter second number: hello
# Traceback (most recent call last):
#  File "d:\Data_Analytics\Modules\PandS\pands-mywork\week03\sub.py", line 8, in <module>
#     y = int(input("Enter second number: "))
# ValueError: invalid literal for int() with base 10: 'hello'.
# burritos.py
# This program will print the number of burritos a person has eaten. The person here is "I".
# author: Kyra Menai Hamilton

# The initial input provided doesn't work.

# message = 'I have eaten ' + 99 + ' burritos.'
# print (message)

# This initial expression causes an error due to the initial statement - 'I have eaten ' + 99 + ' burritos.'
# To modify this so that it works.

# # Using the word "eggs" as a variable name is fine as it begins with a letter, "100" is all numbers and thus an invalid name for a variable.
# Functions that can be used for the:  
# integer - int()
# floating-point number - float(), or
# string version of a value - str().

# Modifying the statement so that it works.

number = int(99)
print("I have eaten {} burritos.".format(number))

# Modified: 11/-2/2025 @ 21:38 - Make it so that someone can input their own value/number of burritos.

# To be fancy about it and get someone to input their own value

# print("How many burritos have you eaten?")
# number = int(input("Enter number: "))
# print("You ate {} burritos.".format(number))
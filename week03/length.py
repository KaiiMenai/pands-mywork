# length.py
# This program will read in a string and output its length.
# author: Kyra Menai Hamilton

# Input string in this case could be words or numbers. Without int in front of numbers they are just a string.

inputstring = input('You will be assked to enter a string. In this case a string can be words or numbers.' '\nEnter a string: ')
stringlength = len(inputstring)
print(f'The length of "{inputstring}" is {stringlength} characters.')

# The output from this is: 
    # You will be assked to enter a string. In this case a string can be words or numbers.
    # Enter a string: 1234
    # The length of "1234" is 4 characters.

# Similarly with words:
    # You will be assked to enter a string. In this case a string can be words or numbers.
    # Enter a string: potato
    # The length of "potato" is 6 characters.

# There are two ways (pribably more) to print the output. The one I'm using is from lab 3.3.
# Similarly to what was done in previous program floor.py, sub.py, and nameAndAge.py, the output can be printed using the format method.   
    # print('The length of "{}" is {} characters.'.format(inputstring, stringlength))

# Giving the output:
    # You will be assked to enter a string. In this case a string can be words or numbers.
    # Enter a string: 1234
    # The length of "1234" is 4 characters.

# References:
# floor.py - https://github.com/KaiiMenai/pands-mywork/blob/main/week03/floor.py
# sub.py - https://github.com/KaiiMenai/pands-mywork/blob/main/week03/sub.py
# nameAndAge.py - https://github.com/KaiiMenai/pands-mywork/blob/main/week02/nameAndAge.py
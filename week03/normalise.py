# normalise.py
# This program will read in a string and output it in lowercase.
    # This program also has leading and trailing spaces removed.
    # It will also output the length of the original string and the normalised string.
# author: Kyra Menai Hamilton

# First for the input string. 
rawstring = input("Please enter a String: ")
normalisedstring = rawstring.strip().lower()

# Used "print(normalisedstring)" to check the input was being normalised correctly.

# Note: if a word is input with a space in the middle by accident, the space will not be removed, as it is neither before or after the word.
# This is because the strip() method only removes leading and trailing spaces.

# Next for the length of the original string and the normalised string.
lenghtofrawstring = len(rawstring)
lenghtofnormalised = len(normalisedstring)

# Finally, print the output.
print(f"The entered String normalised is : {normalisedstring}.")
print(f"We reduced the input String from {lenghtofrawstring} to {lenghtofnormalised} characters.")

# Output: 
    # Please enter a String: PoTATo 
    # The entered String normalised is : potato.
    # We reduced the input String from 7 to 6 characters.

# Using this on sentences however, would result in a lot of letters bring changed into lower case.
# It wouldn't be able to tell the difference in this case between a name and a regular word.
# For example:
    # Please enter a String: Hello I am Kyra
    # The entered String normalised is : hello i am kyra.
    # We reduced the input String from 15 to 15 characters.
# The number of characters remains the same, but the capital letters are removed.
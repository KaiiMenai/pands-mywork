# iseven.py
# Program that asks the user to input a number, and will output to the user whether the number is odd or even.
# author: Kyra Menai Hamilton

# Ask the user to input a number
number = int(input("Please enter a number (as an integer): "))

# Check whether the input is odd or even.

if (number % 2) == 0:
    print(f"{number} is an even number.") # print("The number you entered, {number} is an even number.")
else:
    print(f"{number} is an odd number.")  # print("The number you entered, {number} is an odd number.")

# Output:
# Please enter a number (as an integer): 67
# 67 is an odd number.

# References:
# Python Conditions, W3 schools - https://www.w3schools.com/python/python_conditions.asp
# Python Variables, W3 schools - https://www.w3schools.com/python/python_variables.asp
# worksheet 4.1 - https://vlegalwaymayo.atu.ie/pluginfile.php/1496536/mod_label/intro/Lab%204.1%20if.pdf?time=1676413032542
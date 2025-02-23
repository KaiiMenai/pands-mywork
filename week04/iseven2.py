# iseven2.py
# Modify the program iseven.py so that it will continue to ask the user to enter a number until they enter -1.
# author: Kyra Menai Hamilton

# Ask the user to input a number.
number = int(input("Enter numbers decreasing until a program end message appears. \nPlease enter a number: "))
# Check whether the input is an even number.
while number != -1:
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")
    number = int(input("Please enter a number: "))
print("You have entered -1. The program will now end.")

# Output:
# Please enter a number: 5
# 5 is an odd number.
# Please enter a number: 4
# 4 is an even number.
# Please enter a number: 3
# 3 is an odd number.
# Please enter a number: 2
# 2 is an even number.
# Please enter a number: 1
# 1 is an odd number.
# Please enter a number: 0
# 0 is an even number.
# Please enter a number: -1
# You have entered -1. The program will now end.

# References:
# While Loop examples - https://www.programiz.com/python-programming/while-loop
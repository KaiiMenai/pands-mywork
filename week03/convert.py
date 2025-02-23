# convert.py
# 
# author: Kyra Menai Hamilton 
# Write a program that reads in a float amount of euros, and returns that absolute amount in cent.

# This is similar to the absolute.py program, but instead of returning the absolute value of the number, it will return the number in cent.
# This is also similar to the weekly task  in bank.py, but instead of converting the number cent to euro, it will convert the number to cent.

# Using the basic program from the bank.py task, I went back and added in the parts about the absolute value and float to make it function for reading in a value with or without the - .
# reference below.
    # print("Hello," + "\tPlease enter the following amounts in cents.") # Change this to ask for euros.
    # x = input("Enter amount 1: ")         # Remove the x and y - int not needed.
    # y = input("Enter amount 2: ")         # Add the input as a float.
    # sum = int(x) + int(y)                 # Change this to be for absolute value.
    # def converttoeuro(sum):               # reverse this function to convert to cent.
    #    return '€{:,.2f}'.format(sum/100)

    # txt = f"The sum of these is {converttoeuro(sum)}."
    # print(txt)

# I then used the f-string to format the output - from last week's task and extended reading.

print("Hello," + "\tWhat value would you like to input? Please enter in euros.")
number = float(input("Enter a number:"))
absolutevalue = abs(number)

def converttocent(absolutevalue):
    return '{}'.format(absolutevalue*100)

txt = f"The amount in cent is {converttocent(absolutevalue)}."
print(txt)

# Output:
    # Hello,  What value would you like to input? Please enter in euros.
    # Enter a number:-5.99
    # The amount in cent is 599.0.



# Reference: 
# https://github.com/KaiiMenai/pands-weekly-tasks/blob/main/bank.py

# END
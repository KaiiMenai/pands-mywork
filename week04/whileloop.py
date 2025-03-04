# whileloop.py
# This program demonstrates the use of a while loop in Python.
# author: Kyra Menai Hamilton

# A while loop is used to execute a block of code repeatedly as long as a condition is true.
# The while loop is used when you do not know how many times a block of code will need to be executed.
# The while loop is used when you want to execute a block of code repeatedly based on a condition.
# The while loop is used when you want to execute a block of code repeatedly until a condition is met - whether that is a number, a true/false statement, or a string.  

# In this example, we will use a while loop to print numbers from 1 to 5.
# The while loop will continue to execute as long as the condition is true.
# The condition is x <= 5.
# The condition is true as long as x is less than or equal to 5.
# The condition is false when x is greater than 5.
# The while loop will stop executing when the condition is false.

number = 1
while number <= 5:
    print(number)
    number += 1

print ("End of basic loop example.")


# Output:
    # 1
    # 2
    # 3
    # 4
    # 5
    # End of basic loop example.
    # This will print numbers from 1 to 5 as long as the condition is true.

# Note: if the loop condition is always true, the loop will run indefinitely, that ism it wuill be a potentially infinite loop.
# To avoid this, you can use a break statement to exit the loop when a certain condition is met.
# The break statement is used to exit the loop when a certain condition is met.
# The break statement is used to exit the loop when a certain condition is true.
# The break statement is used to exit the loop when a certain condition is met, and the loop will not continue to execute.

# In this example, we will use a while loop to print numbers from 1 to 5.
# The while loop will continue to execute as long as the condition is true.
# The condition is x <= 5.
# The condition is true as long as x is less than or equal to 5.
# The condition is false when x is greater than 5.
# The while loop will stop executing when the condition is false.

number = 1
while number <= 5:
    print(number)
    if number == 3:
        break
    number += 1

print ("End of break example.")

# Output:
    # 1
    # 2
    # 3
    # End of break example.
    # This will print numbers from 1 to 3 as long as the condition is true.
    # The loop will exit when the condition number == 3 is met.

# Another was to exit a loop is to use the continue statement.
# The continue statement is used to skip the rest of the code inside a loop for the current iteration only.

# In this example, we will use a while loop to print numbers from 1 to 5.
# The while loop will continue to execute as long as the condition is true.
# The condition is x <= 5.
# The condition is true as long as x is less than or equal to 5.
# The condition is false when x is greater than 5.
# The while loop will stop executing when the condition is false.

number = 0
while number < 5:
    number += 1
    if number == 3:
        continue
    print(number)

print ("End of continue example.")

# Output:
    # 1
    # 2
    # 4
    # 5
    # End of continue example.
    # This will print numbers from 1 to 5 as long as the condition is true.
    # The loop will skip the number 3 and continue to execute

# References:
# Real Python - https://realpython.com/python-while-loop/
# Python.org - https://docs.python.org/3/tutorial/introduction.html
# Python.org - https://docs.python.org/3/tutorial/controlflow.html
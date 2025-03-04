# whileelse.py
# This program demonstrates the use of a while loop with an else statement in Python.
# author: Kyra Menai Hamilton

# A while loop is used to execute a block of code repeatedly as long as a condition is true.
# The while loop is used when you do not know how many times a block of code will need to be executed.
# The while loop is used when you want to execute a block of code repeatedly based on a condition.
# The while loop is used when you want to execute a block of code repeatedly until a condition is met - whether that is a number, a true/false statement, or a string.
# The else statement is used to execute a block of code when the condition is false.
# The else statement is used to execute a block of code when the condition is false, and the loop will not continue to execute.
# The else statement is used to execute a block of code when the condition is false, and the loop has finished executing.

import random
import time

# In this example, we will use a while loop to generate random numbers until a certain condition is met.
# The while loop will continue to execute as long as the condition is true.
# The condition is x != 5.
# The condition is true as long as x is not equal to 5.
# The condition is false when x is equal to 5.
# The while loop will stop executing when the condition is false.
# The else statement is used to print a message when the condition is false.
# The else statement is used to print a message when the condition is false, and the loop has finished executing.

MAX_RETRIES = 5
attempts = 0

while attempts < MAX_RETRIES:
    attempts += 1
    print(f"Attempt {attempts}: Connecting to the server...")
    # Simulating a connection scenario
    time.sleep(0.3)
    if random.choice([False, False, False, True]):
        print("Connection successful!")
        break
    print("Connection failed. Retrying...")
else:
    print("All attempts failed. Unable to connect.")

# Output:
    # Attempt 1: Connecting to the server...
    # Connection failed. Retrying...        
    # Attempt 2: Connecting to the server...
    # Connection failed. Retrying...
    # Attempt 3: Connecting to the server...
    # Connection successful!

# In this example, the while loop continues to execute until the condition is false.
# The condition is false when the connection is successful.
# The BREAK statement is used to exit the loop when the connection is successful.
# The ELSE statement is used to print a message: 
    # when the condition is false,
    # and the loop has finished executing.

# References:
# https://s3-us-west-2.amazonaws.com/python-notes/a-whirlwind-tour-of-python-2.pdf
# https://www.w3schools.com/python/python_while_loops.asp
# https://www.w3schools.com/python/python_for_loops.asp
# https://realpython.com/python-while-loop/

# END

# loopyloop.py
# This python file contains do-while, event, and unintentional loop examples.
# author: Kyra Menai Hamilton

# Emulating Do-While Loops

# A do-while loop is a control flow statement that executes its code block at least once,
    # regardless of whether the loop condition is true or false.

# Example using a user input loop:

while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:
        break

# Output:
    # Enter a positive number: 1
    # 1
    # Enter a positive number: 4
    # 4
    # Enter a positive number: -1
    # -1

# this loop takes the user input using the built-in input() function. 
# The input is then converted into an integer number using int(). 
# If the user enters a number that’s 0 or lower, then the break statement runs, and the loop terminates.

# Note that to emulate a do-while loop in Python, the condition that terminates the loop goes at the end of the loop, and its body is a break statement. 
# It’s also important to emphasize that in this type of loop, the body runs AR LEAST once.

# Using while Loops for Event Loops

# Another common and extended use case of while loops in Python is to create event loops.
    # (Which are infinite loops that wait for certain actions known as events.)
# Once an event happens, the loop dispatches it to the appropriate event handler.

# Some classic examples of fields where you’ll find event loops include the following:
    # Graphical user interface (GUI) frameworks
    # Game development
    # Asynchronous applications
    # Server processes

# Example (number guessing game):

from random import randint

LOW, HIGH = 1, 10

secret_number = randint(LOW, HIGH)
clue = ""

# Game loop
while True:
    guess = input(f"Guess a number between {LOW} and {HIGH} {clue} ")
    number = int(guess)
    if number > secret_number:
        clue = f"(less than {number})"
    elif number < secret_number:
        clue = f"(greater than {number})"
    else:
        break

print(f"You guessed it! The secret number is {number}")

# Output: 
    # Guess a number between 1 and 10  7
    # Guess a number between 1 and 10 (less than 7) 5
    # Guess a number between 1 and 10 (less than 5) 3
    # Guess a number between 1 and 10 (less than 3) 1 
    # Guess a number between 1 and 10 (less than 3) 2
    # You guessed it! The secret number is 2

# In this example, the game loop runs the game logic. 
# First, it takes the user’s guess with input(), converts it into an integer number, and checks whether it’s greater or less than the secret number. 
# The else clause executes when the user’s guess is equal to the secret number. 
# In that case, the loop breaks, and the game shows a winning message.


# Exploring Infinite while Loops

# Intentional infinite loops are powerful tools commonly used in programs that need to run continuously until an external condition is met, such as game loops, server processes, and event-driven apps like GUI apps or asynchronous code.

# In contrast, unintentional infinite while loops are often the result of some kind of logical issue that prevents the loop condition from ever becoming false. For example, this can happen when the loop:
    # Fails to update a condition variable
    # Uses a condition that’s logically flawed

# In these cases, the loop erroneously continues to run until it’s terminated externally.

## Unintentional Infinite Loops

## Intentional Infinite Loops

# Examples: https://realpython.com/python-while-loop/#exploring-infinite-while-loops

# References:

# https://realpython.com/python-while-loop/#emulating-do-while-loops
# https://realpython.com/python-while-loop/#using-while-loops-for-event-loops
# https://realpython.com/python-while-loop/#exploring-infinite-while-loops

# END

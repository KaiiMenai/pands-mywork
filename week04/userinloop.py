# userinloop.py
# This program explores wgat happens with user input in command lines in a while loop in Python.
# author: Kyra Menai Hamilton

# Getting user input from the command line is a common use case for while loops in Python. 
# Consider the following loop that takes input using the built-in input() functions. 
# The loop runs until you type the word "stop":

line = input("Type some text: ")

while line != "stop":
    print(line)
    line = input("Type some text: ")

# The input() function asks the user to enter some text. 
# Then, you assign the result to the line variable. 
# The loop condition checks whether the content of line is different from "stop", in which case, the loop body executes. 
# Inside the loop, you call input() again. 
# The loop repeats until the user types the word stop.

# This example works, but it has the drawback of unnecessarily repeating the call to input(). 
# You can avoid the repetition using the walrus operator as in the code snippet below:

while (line := input("Type some text: ")) != "stop":
    print(line)

# Output:
    # Type some text: Python
    # Python
    # Type some text: Walrus
    # Walrus
    # Type some text: stop

# In this updated loop, you get the user input in the line variable using an assignment expression. 
# At the same time, the expression returns the user input so that it can be compared to the sentinel value "stop".

# Traversing Iterators With while Loops

# Using a while loop with the built-in next() function may be a great way to fine-control the iteration process when working with iterators and iterables.
# To give you an idea of how this works, you’ll rewrite a for loop using a while loop instead. 
# Example:

requests = ["first request", "second request", "third request"]

print("\nWith a for loop")
for request in requests:
    print(f"Handling {request}")

print("\nWith a while loop")
it = iter(requests)
while True:
    try:
        request = next(it)
    except StopIteration:
        break

    print(f"Handling {request}")

# Output:
    # With a for loop
    # Handling first request
    # Handling second request
    # Handling third request

    # With a while loop
    # Handling first request
    # Handling second request
    # Handling third request

# END
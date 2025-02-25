# shortifelse.py
# This program demonstrates the use of a short if-else statement in Python.
# author: Kyra Menai Hamilton

# The short if-else statement is a one-liner that allows you to execute a statement if a condition is true, and another statement if the condition is false.
# It is used when you have only one statement to execute

a = 2
b = 330
print("A") if a > b else print("B")

# Output:
    # B
    # This will print "B" as a is not greater than b.

# With the short if-else statement, you can execute multiple else statements on the same line.
# This technique is known as Ternary Operators, or Conditional Expressions.

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Output:
    # =
    # This will print "=" as a is equal to b.

# END
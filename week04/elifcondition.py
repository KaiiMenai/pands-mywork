# elifcondition.py
# This program explores the use of elif conditions in Python
# author: Kyra Menai Hamilton

# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# These conditions can be used in several ways, most commonly in "if statements" and loops.

# Elif is short for "else if". 
# It allows us to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions is TRUE.
# If the condition for if is False, it checks the condition of the next elif block and so on.
# If all the conditions are False, the body of else is executed.
# Only one block among the several if...elif...else blocks is executed according to the condition.
# The if block can have only one else block. But it can have multiple elif blocks.
# It is important to include an indentation after the colon in the if statement.
# This is to show that the code that follows is part of the if statement.

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# Output:
    # a and b are equal
    # This will print "a and b are equal" as a is equal to b.

# The elif block is executed only if the if condition is False.

# End
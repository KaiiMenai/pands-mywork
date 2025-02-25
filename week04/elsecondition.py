# elsecondition.py
# This program explores the use of else conditions in Python
# author: Kyra Menai Hamilton

# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "else statement" is used in conjunction with an "if statement".
# An "else statement" contains the block of code that executes if the conditional expression in the "if statement" resolves to 0 or a FALSE value.
# The "else statement" is an optional statement and there could be at most only one "else statement" following "if".
# The "else statement" is always associated with the closest "if statement".
# An "else statement" can be used without an "if statement".
# If there is an "else statement" without an "if statement", it will be executed irrespective of the condition.

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Output:
    # a is greater than b
    # This will print "a is greater than b" as a is greater than b.

# Without the elif condition, the else statement will be executed.
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")

# END
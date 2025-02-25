# nestedif.py
# This program demonstrates the use of nested if statements in Python.
# author: Kyra Menai Hamilton

# Nested if statements are if statements that are nested inside another if statement.
# Nested if statements are used to check multiple conditions.
# Nested if statements are used when you have multiple conditions to check.

# In this example, we will use nested if statements to check multiple conditions.

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# Output:
    # Above ten,
    # and also above 20!
    # This will print "Above ten," and "and also above 20!" as the condition is true.

y = -15
if y == 0:
    print(y, "is zero")
elif y > 0:
     print(y, "is positive")
elif y < 0:
    print(y, "is negative")
else:
    print(y, "is unlike anything I've ever seen...")

# Output:
    # -15 is negative
    # This will print "-15 is negative" as the condition is true.

# Notes: 
# The first if statement checks if y is equal to 0.
# The elif statement checks if y is greater than 0.
# The elif statement checks if y is less than 0.
# The else statement is used to catch anything that is not caught by the preceding conditions.
# In this example, y is less than 0, so the "is negative" statement is printed.

# The use of : is important in Python as it is used to indicate the start of a block of code.
# The indentation is also important in Python as it is used to define the scope of the code.
# The code that is indented after the : is part of the block of code.
# The code that is not indented is outside the block of code.

# END
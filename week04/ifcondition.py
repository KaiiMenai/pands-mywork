# ifcondition.py
# This program explores the use of if conditions in Python.
# author: Kyra Menai Hamilton

# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# These conditions can be used in several ways, most commonly in "if statements" and loops.

# It is important to include an indentation after the colon in the if statement. 
# This is to show that the code that follows is part of the if statement.
# Without the indentation, the code will not run correctl, and will show an error.

a = 33
b = 200
if b > a:
  print("b is greater than a") # The indentation here is important.

# Output:
    # b is greater than a  
    # This will print "b is greater than a" as 200 is greater than 33.

# Here is an example of an if statement that will not run correctly due to the lack of indentation.

# a = 33
# b = 200
# if b > a:
# print("b is greater than a") # There will be an error here as there is no indentation.

# End
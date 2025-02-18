# stringfothmat.py
# This program is to explore the different ways to format strings in Python.
# author: Kyra Menai Hamilton


# Interpolating and Formatting Strings in Python
    # 1. String interpolation
# String interpolation - generating strings by inserting other strings or objects into specific places in a base string or template.
# https://realpython.com/python-string-formatting/#interpolating-and-formatting-strings-in-python

name = "Kyra"
print(f"Hello, {name}!") # Initially I forgot to add the f in front of the string. but figured it out when I got the output: Hello, {name}!
# Output:
    # Hello, Kyra!

    # 2. String formatting
# String formatting - a way to insert variables into strings.

print(f"The number is {42}.") 
    # Output: The number is 42.
a = 5
b = 10
print(f"The sum of {a} and {b} is {a + b}.")
# Output: 
    # The sum of 5 and 10 is 15.

# Using the Formatting Mini-Language With F-Strings
# When you use f-strings to create strings through interpolation, you need to use replacement fields. In f-strings, you can define a replacement field using curly brackets ({}).
# https://realpython.com/python-string-formatting/#using-the-formatting-mini-language-with-f-strings

debit = 300.00
credit = 450.00

print(f"Debit: €{debit}, Credit: €{credit}, Balance: €{credit - debit}.")
# Output: 
    # Debit: €300.0, Credit: €450.0, Balance: €150.0.

# Inside the brackets, you can insert Python objects and expressions. 
# In this example, you’d like the resulting string to display the currency values using a proper format. 
# However, you get a string that shows the currency values with at most one digit on its decimal part.
# To fix this.
print(f"Debit: €{debit:.2f}, Credit: €{credit:.2f}, Balance: €{credit - debit:.2f}.")
# Output:
    # Debit: €300.00, Credit: €450.00, Balance: €150.00.
# The :.2f part of the replacement field is a format specification.

# https://realpython.com/python-f-strings/
# https://realpython.com/python-string-formatting/#formatting-strings-with-f-strings-a-practical-example

# Note:  If you supplied the string :
# use f"{variable}" pattern
# else : 
# use string templates (This stops malicious code injection)
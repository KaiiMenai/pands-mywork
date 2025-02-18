# intfloatcomplex.py
# This program is to test the different types of numbers in Python. 
# author: Kyra Menai Hamilton

# I wanted to further explore different types of Python numbers.

x = 1    # int
y = 2.8  # float
z = 1j   # complex

# Display the data type of each number.

print(type(x))
print(type(y))
print(type(z))

# Output:
    # <class 'int'>
    # <class 'float'>
    # <class 'complex'>

# Definition of each type of number:
    # Int/Integer: A whole number, positive or negative, without decimals, of unlimited length.
    # Float: A floating point number, positive or negative, containing one or more decimals. This can also be scientific numbers with an "e" to indicate the power of 10.  
    # Complex: A number with a real and imaginary part, i.e. use of the letter "i".

# Converting from one type to another type can be done using int(), float(), and complex().

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Output:
    # 1.0
    # 2
    # (1+0j)
    # <class 'float'>
    # <class 'int'>
    # <class 'complex'>

# Making a random number in Python. 
# This can be done using the random module that is built in Python.
import random

print(random.randrange(1, 10))
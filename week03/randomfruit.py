# randomfruit.py
# This program spits (prints) out random fruits.
# author: Kyra Menai Hamilton

import random
fruits = ['Apple', 'Kiwi', 'Grape', 'Pear']

# The square brackets indicate a list [].
# We want a random number between 0 and lenght-1.

index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("A random fruit: {}.".format(fruit))

# There will be a way in future week classes to make this tidyer.
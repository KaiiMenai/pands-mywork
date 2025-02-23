# randomfruit2.py
# This program spits (prints) out random fruits.
# author: Kyra Menai Hamilton

import random
fruits = ('Apple', 'Kiwi', 'Grape', 'Pear')

# Here the square brackets for list [], have been swapped for round brackets () for tuple.
# Because the list isn't changed during the process/program, then the tuple () should have been used from the start.
# We want a random number between 0 and lenght-1 (same as before).

index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("A random fruit: {}.".format(fruit))

# END
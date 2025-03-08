# topthree.py
# This program will generate 10 random numbers between 0 and 100.
# It will print out the 10 numbers, and it will then print out the top three.
# author: Kyra Menai Hamilton

import random

# Giving the parameters of the numbers that we want generated.

howmany = 10    # Want 10 random numbers.
tophowmany = 3  # Want the top 3.
rangefrom = 0   # Want to start at 0.
rangeto = 100   # Want to stop at 100.

numbers = []    # Want a list to be able to store and then manipulate the numbers (select the top 3).

for i in range(0, howmany): # For the integers in the range, giving 10 outputs.
    numbers.append(random.randint(rangefrom, rangeto))  # the range of numbers is between 0 and 100
print(f"{howmany} random numbers\t {numbers}")  # print the 10 random numbers from the range in a list format.

topones = numbers.copy()        # What are the topones in the list.

topones.sort(reverse = True)    # Sort this list in reverse.
print(f"The top {tophowmany} are \t\t {topones[0:tophowmany]}.") # Initially the example was missing the f function that would make it work.
                                                                 # So the output for this line was "The top {tophowmany} are                 {topones[0:tophowmany]}.".

# Output:
    # 10 random numbers        [15, 52, 42, 80, 90, 22, 100, 48, 60, 63]
    # The top 3 are            [100, 90, 80].

# END
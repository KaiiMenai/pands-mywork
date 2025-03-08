# countersentinel.py
# This program is for exploring and illustrating the differences between Counter and Sentinel Controlled loops.
# author: Kyra Menai Hamilton

#while condition:
#    statements

# There are generallty two types of loops
    # Counter Controled
        # We usualy use for loops for counter conttroled loops. 
        # This is where a loop will be run X times, or whilst a value is different from X number.

    # Sentinal Controled
        # When reading in from a user, one pattern is:
            # read in from the user, check the while, and then read again in the body of the while loop. 
        # Need to be careful of infinite looping
        # To prevent infinite loops, make sure you modify what you are checking.

# Advised:
    # Not to have AND's or OR's inside the loop as it will make it more complicated.
    # Keep WHILE loop logic as simple as possible.
    # BREAK and CONTINUE are other logic that can be used in a while loop.

# Three MAIN parts of loops:
    # 1 - INITIALISE conditions variables
    # 2 - CHECK condition
    # 3 - CHANGE condition variables

# Counter Controlled Loop

count = 0
while (count < 10):
    print("Count is ", count)
    count = count + 1

print ("At the end count is ", count)

count = 10
while count >=0:
    print ("Countdown ", count)
    count -= 1
print("Blast off")

# Sentinel Controlled Loop

val = input("Type something (q to quit):")
while val != 'q':
    print ("hi mom")
    val = input("q to quit:")

print("All done")

# END
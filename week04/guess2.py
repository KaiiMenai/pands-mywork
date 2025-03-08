# guess2.py
# Modification of program guess1.py. 
# In this program, it will tell the user if their input is too high or too lw each time they guess. 
    # A tip here is to use an "IF" statement inside the loop. 
# author: Kyra Menai Hamilton

numbertoguess = 30  # This is the number the program wants the user to guess.

guess = int(input("Please guess the number: ")) # Enter the number as an integer following the prompt.
while guess != numbertoguess:                   # While the number inputted does not equal the numbertoguess (i.e. 30)...
    if guess < numbertoguess:                   # If the number is less than 30 (numbertoguess)
        print ("Too low.")                      # ...the output will show as "Too low.".
    else:                                       # We know that if it isn't too low or equal to 30 (numbertoguess)...
        print ("Too high.")                     # ...then it must be "Too high."
    guess = int(input("Please guess again: "))  # It will then prompt the user to guess again.

print ("Well done! Yes, the number was", numbertoguess)    # When the user guesses correctly, this message will show on screen.

# Output:
    # Please guess the number: 3
    # Too low.
    # Please guess again: 50
    # Too high.
    # Please guess again: 30
    # Well done! Yes, the number was 30

# This can also be run when the program generates a random number.
# Extra: get the program to generate a random number between 0 and 100 to guess.

import random       # Import the random number package.

start = int(0)      # Using logic from randomGenerator.py (link below)
stop = int(100)     # ...create start and stop points of 0 and 100.

guessnumber = random.randint(start, stop)

userguess = int(input("Please guess the number: ")) # Enter the number as an integer following the prompt.
while userguess != guessnumber:                     # While the number inputted does not equal the guessnumber...
    if userguess < guessnumber:                     # If the number is less than the random guessnumber...
        print ("Too low.")                          # ...the output will show as "Too low.".
    else:                                           # We know that if it isn't too low or equal to guessnumber...
        print ("Too high.")                         # ...then it must be "Too high."
    userguess = int(input("Please guess again: "))  # It will then prompt the user to guess again (and again).

print ("Well done! Yes, the number was", guessnumber)  

# Output:
    # Please guess the number: 30
    # Too high.
    # Please guess again: 20
    # Too low.
    # Please guess again: 25
    # Too high.
    # Please guess again: 21
    # Too low.
    # Please guess again: 22
    # Too low.
    # Please guess again: 23
    # Well done! Yes, the number was 23

# References:
# randomGenerator.py - https://github.com/KaiiMenai/pands-mywork/blob/main/week03/randomGenerator.py
# Lab 4.2 - https://vlegalwaymayo.atu.ie/pluginfile.php/1496536/mod_label/intro/Lab%204.2%20loops.pdf?time=1676413047731

# END
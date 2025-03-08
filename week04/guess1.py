# guess1.py
# This program will promps the user to guess a number.
# The program will keep prompting the user to guess a number until the user gets the correct number.
# author: Kyra Menai Hamilton

numbertoguess = 30  # This is the number the program wants the user to guess.

guess = int(input("Please guess the number: "))  # Enter the number as an integer following the prompt.
while guess != numbertoguess:                   # While the number inputted does not equal the numbertoguess (i.e. 30)...
    print ("Wrong!")                             # ...the output will show as "Wrong".
    guess = int(input("Please guess again: "))   # It will then prompt the user to guess again.

print ("Well done! Yes, the number was", numbertoguess)    # When the user guesses correctly, this message will show on screen.

# Output:
    # Please guess the number: 3
    # Wrong!
    # Please guess again: 30
    # Well done! Yes, the number was 30

# After correcting some spacing to ensure that there was continuity in styling the output was as above.

# END
# average.py
# This program will keep reading the numbers input by the user until the user enters a 0.
# The program will then append the inputted numbers into a list.
# This will be printed out prior to the average of these numbers being calculated..
# author: Kyra Menai Hamilton

numbers = [] # This is a list called numbers.

number = int(input("Enter a number (0 to quit): ")) # Ask the user to enter a number.

while number != 0:              # While the inputted number does not equal 0...
    numbers.append(number)      # ...enter the number into the appended list for numbers.

    number = int(input("Enter another number (0 to quit): ")) # Ask for another number, program will read and check if 0.

for value in numbers:           # Print the list within numbers.
    print (value)

average = float(sum(numbers)) / len(numbers) # We want the average as a floating point number.
                                                # Get the average of the listed numbers.
print(f"The average is {average}.")  # Print the average value of the numbers.

# Output:
    # Enter a number (0 to quit): 33
    # Enter another number (0 to quit): 34
    # Enter another number (0 to quit): 0
    # 33
    # 34
    # The average is 33.5.

# END
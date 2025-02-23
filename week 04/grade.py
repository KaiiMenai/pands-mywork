# grade.py
# Program that asks the user to input a student's percentage mark, and will output the corresponding grade. 
# RThe program will also check that the percentage is valid.
# author: Kyra Menai Hamilton

# Grading system: 
# • Under 40% => Fail
# • Between 40% and 49% => Pass
# • Between 50% and 59% => Merit 2
# • Between 60% and 69% => Merit 1
# • Over 70% => Distinction

# Enter the percentage: 67
# Merit2

# Ask the user to input a percentage mark
percentage = float(input("Please enter the student's percentage mark: "))
print(percentage)
# Check whether the input is a valid percentage. Need to be careful with the order of the if statements.
if percentage < 0 or percentage > 100:   # Will show an error message if the percentage is less than 0 or more than 100.
    print("Invalid percentage mark. Please enter a number between 0 and 100.")
elif percentage < 40:   # The percentage is less than 40.
    print("Fail")
elif percentage < 50:   # The percentage between 40 and 49.
    print("Pass")
elif percentage < 60:   # The percentage between 50 and 59.
    print("Merit 1")
elif percentage < 70:   # The percentage between 60 and 69.
    print("Merit 2")
else:                   # As there are no other values left, ELSE is used here as the percentage is over 70%.
    print("Distinction") 

# Output:
    # Please enter the student's percentage mark: 67
    # 67.0
    # Merit 2

# For each percentage mark entered, the corresponding grade will be displayed.
# To test each statement, I entered the following percentage marks:
# Please enter the student's percentage mark: -1
    # -1.0
    # Invalid percentage mark. Please enter a number between 0 and 100.

# Please enter the student's percentage mark: 25
    # 25.0
    # Fail

# Please enter the student's percentage mark: 43
    # 43.0
    # Pass

# Please enter the student's percentage mark: 56
    # 56.0
    # Merit 1

# Please enter the student's percentage mark: 67
    # 67.0
    # Merit 2

# Please enter the student's percentage mark: 89
    # 89.0
    # Distinction

# END
# grade2.py
# Modification of grade.py to include a function that will round the grade up/down dependingon the percentage entered.
# author: Kyra Menai Hamilton

# Now to adapt the program.
# In practice the percentages are rounded ie 69.5 gets rounded to 70 so is
# equal to a Distinction. 
# For this  I will modify the input to always round UP the unput to the nearest whole number.

# Ask the user to input a percentage mark
percentage = float(input("Please enter the student's percentage mark: "))
print(f"The student's grade is {percentage:.2f} %.")
# Round the percentage up to the nearest whole number.
rounded_percent = round(percentage)
print(f"The student's rounded grade is {rounded_percent:.2f} %.")

# It may be possible to do a check to see if the percentage is a whole number and if not round it up to the nearest whole number.
# Using the math module to round up the percentage to the nearest whole number.
# But I will leave it as is for now.

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



# END
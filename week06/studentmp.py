# studentmp.py
# A program that reads in students and their modules and grades from a file.
# The program then prints this data out, sorted by student name.
# author: Kyra Menai Hamilton

import pandas as pd
import numpy as np


# Ask the user what they would like to do.

print("What would you like to do? \nPlease select from the following options: ")
print("\t(a) Add new student details")
print("\t(v) View student details")
print("\t(q) Quit)")
choice = input("Type one letter (a/v/q): ").strip()


# Initialize an empty list to store all students' details
students = []

# Continue to read in student details until a blank student ID is entered
while True:
    # Read the student's name (or ID)
    identity = input("Please enter the student's name (or leave empty and press Enter to finish): ")
    if not identity.strip():  # Break if the student name/ID is empty or whitespace
        break

    # Create a dictionary for the current student
    student = {
        "name": identity,
        "modules": []
    }

    # Continue to read in course names and grades for this student until a blank course name is entered
    while True:
        courseid = input("Please enter the course name (or leave empty and press Enter to finish): ")
        if not courseid.strip():  # Break if the course name is empty or whitespace
            break

        # Read the grade for the entered course
        mark = input(f"Please enter the student's grade for {courseid}: ")

        # Add the module details to the student's modules list
        student["modules"].append({
            "course": courseid,
            "mark": mark
        })

    # Add the completed student dictionary to the list of students
    students.append(student)

# Print out all students' details
print("\nAll Students:")
for student in students:
    print("Student: {}".format(student["name"]))
    for module in student["modules"]:
        print("\t{} \t: {}".format(module["course"], module["mark"]))
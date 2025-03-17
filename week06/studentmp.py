# studentmp.py
# A program that reads in students and their modules and grades from a file.
# The program then prints this data out, sorted by student name.
# author: Kyra Menai Hamilton

# Ask the user what they would like to do.

def display_menu():
    print("What would you like to do? \nPlease select from the following options: ")
    print("\t(a) Add new student details")
    print("\t(v) View student details")
    print("\t(q) Quit)")
    choice = input("Type one letter (a/v/q): ").strip()

    return choice
# Test that this actually works.
# choice = display_menu()
# print(f"You chose {choice}.")

# Here we have defined the choices and also reiterate what choice the user has made.

# Next we will add the ability to add a student.
# A function will be created to do this, and it will need to be called when the user selects 'a'.

# def do_add():
    # print("In adding.")         # This is just a placeholder for now.

# Make an empty list to store all students' details
students = []

def do_add(students):
    current_student = {}
    current_student["name"] = input("Enter student name: ")
    current_student["modules"] = read_modules()

# Add the completed student dictionary to the list of students
    students.append(current_student)

# Test what has been done thus far.
# do_add(students)
# do_add(students)
# print (students)

# Need to add a placeholder for modules.

def read_modules():
    modules = []
    module_name = input("\tEnter the first module name (blank to quit): ").strip()
    while module_name != "":
        module = {}
        module["name"] = module_name
        module["grade"] = int(input("\tEnter the grade: "))
        modules.append(module)
        module_name = input("\tEnter the next module name (blank to quit): ").strip()
    return modules

# Next we will add the ability to view a student.
# def do_view():
#     print("In viewing.")        # Again, just a placeholder, will be elaborated later.

# Make the output more readable.
def do_view(students):
    for current_student in students:
        print(f"Student: {current_student['name']}")
        for module in current_student["modules"]:
            print(f"\tModule: {module['name']}, \tGrade: {module['grade']}")

# Now we will add the ability to quit the program.
def do_quit():
    quit()

# Now to add the details.
# The main program loop

choice = display_menu()
while choice != 'q':            # While choice doesn't equal 'q', the program will continue to run.
    if choice == 'a':           # If the choice is 'a', the program will run the do_add function.
        do_add(students)
    elif choice == 'v':         # If the choice is 'v', the program will run the do_view function.
        do_view(students)
    elif choice != 'q':         # If the choice is not 'q', the program will print an error message.
        print("\n\nPlease select either a, v or q.")
    choice = display_menu()

# END
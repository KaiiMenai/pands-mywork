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

choice = display_menu()
print(f"You chose {choice}.")

# Here we have defined the choices and also reiterate what choice the user has made.

# Next we will add the ability to add a student.
# A function will be created to do this, and it will need to be called when the user selects 'a'.

def do_add():
    print("In adding.")         # This is just a placeholder for now.
    
# Next we will add the ability to view a student.
def do_view():
    print("In viewing.")        # Again, just a placeholder, will be elaborated later.
    
# Now we will add the ability to quit the program.
def do_quit():
    print("Quitting.")

# Now to add the details.
# The main program loop is as follows:

choice = display_menu()
while choice != 'q':            # While choice doesn't equal 'q', the program will continue to run.
    if choice == 'a':           # If the choice is 'a', the program will run the do_add function.
        do_add()
    elif choice == 'v':         # If the choice is 'v', the program will run the do_view function.
        do_view()
    elif choice != 'q':         # If the choice is not 'q', the program will print an error message.
        print("\n\nPlease select either a, v or q.")
    choice = display_menu()

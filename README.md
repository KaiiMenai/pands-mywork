# My work for the Programming and Scripting module
Content within will reflect progress throughout the module.

## Week 1

Gitignore and initial firsthello.py created.

Commiting and making files:
- Commands used = "git clone PASTED.URL", "git config pull.rebase false", "git pull", "git add .", "git push", "git commit -m "test"", "ls", "cd (..)", 

Order of usage in Cmder. *Don't forget to commit and push in VSCode first*
 - go to file where updates were made.
 - "ls"
 - "git config pull.rebase false"
 - "git add ."
 - "git commit -m "COMMENT WHAT WAS DONE""
 - "git push"

 Probably too many steps, but checking through this list of commands/prompts helps to determine the steps needed/what is missing.


## Week 2

Started out adding a week02 folder to the pands-mywork file. Into the folder seveal python programs and iterations/modifications were made.

 - Made helloworld.py which prints a basic "Hello World!" output.
 - New Python program hello.py created. This was then modified to say my name after hello, and then syntax errors added, then removed to see the error given.
 - multiply.py created to find answer to multiplication. Ptiny logic added to view answer.
 - New program hello2.py added allowing use of user input response to modify output name salutation, and \n command added to put the greeting on a new line. Optional alternative input method mentioned in prog. comments.
 - Program for printing a number one higher than that inputted made (addOne.py). integer function (int()) included so that pyython sees the input as a number and not just as a text input.
 - A program modified from hello2.py adding in an age variable. This program initially printed the output on seperate lines following the initial input prompts, it was then modified to have "tab" between the output fields instead.
 - Basic program seventeen.py was made to print the answer for 21-4 (which is 17).
 - Program noequal.py was made to demonstrate the comparator (equality operator) function of == which would result in a FALSE or TRUE answer depending on the input. In this case the output was FALSE as 2=/=3.
- Exploring further functions and modifiers was done in the money.py program. In this program several outputs were obtained from using Python string formatting.
    - Basic number price printing.
    - A placeholder was added in for the price allowing it to be changed outside of the function.
    - A modifier was added followed by the legal formatting type .2f which gave an output of a fixed point number with 2 decimal places (dp).
    - Values were formatted directly rather than by placeholder. (i.e. {95:.2f}) giving 95.00.
    - A math operation was performed within the placeholder ({20*60}) giving 1200.
    - A math operation was performed on the variables price (50) and tax (0.23), (txt = f"The price is {price + (price * tax)} euros").
    - The modifier was added back in to give the output to 2 decimal places, (txt = f"The price is {price + (price * tax):,2f} euros").
    - Testing the use of an if...else statement was conducted for "Expensive" and "Cheap" as outputs for prices over or under 70 euros, respectively.
    - In the same program file all price and tax input/txt/print was changed into note form.
    - Tested the use of upper() to change the word raspberries into upper case in a statement.
    - Fruit statement changed to note format.
    - Practiced use of inputting/creating own function through the use of a function converting feet to meters.

All files commited and pushed to GitHub.

END
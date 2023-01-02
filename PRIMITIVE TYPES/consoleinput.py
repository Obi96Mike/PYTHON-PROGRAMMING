# CONSOLE INPUT - allowing user to type something in the console and then capturing what they are typing and using that value somehow.
# input() gathers user input from the command line. It always returns a str object which will need to be converted to a different type at times. e.g., int if you expect the user input to be an integer.
# TYPE CONVERSION - converts one data type to another. type() returns the class that an object is constructed from; it returns a class of whatever argument one passes in, to get the data type of a variable.
# int(x), float(x), string(x), bool(x)
# bool(x), converts input into equivalent boolean values. Values that are considered truthy or falsy when they have to be evaluated in some kind of boolean context.
# bool(0), bool("") - empty string, None ; Falsy values in Python
# On running, go to Terminal (Ctrl + Backspace). First cd 'Folder Name'. Then type python strings.py in Windows or python3 strings.py in Mac or Linux
x = input("x: ")
print(type(x))
y = int(x) + 1
# Formatted string
print(f"x: {x}, y: {y}")

user_name = input("What is your name? ")
print("Hello", user_name + "!")

# Sample Program Execution Example
# What is your name? Obi
# Hello, Obi
name = input("What is your name? ")
print('Hello,', name)

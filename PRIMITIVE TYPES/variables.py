# VARIABLES - a way to access or manipulate data
# In dynamically typed languages, e.g., Python, variable doesn't need to have a type and doesn't need to be declared
# Unlike statically typed languages e.g., Java, C++ where variable has a type and has to be declared.

# VARIABLE NAMING RULES
# All variables must be meaningful and descriptive
# Lower case letters used to name variables
# Underscore is used to separate multiple words
# There is a space around equal signs
# It must start with a letter; must not start with a number
# It must not contain any special characters
# Python's reversed keywords e.g., print, lambda, import, return cannot be used as a variable name. Reversed keywords are words that are used for various operations in the language

# snake_case
# camelCase
# PascalCase
students_count = 1, 000  # int
rating = 4.99  # float
is_published = True  # bool
course_name = "Python programming"  # string


x = 5
y = "Python Programming"
z = True
x = y  # "Python Programming"
y = z  # True
z = x  # "Python Programming"
print(z)

# A program that declares three variables: x, y and z, equal to 2, 7, and True, respectively. Your program should then print the values of x, y and z on one line, separated by spaces.
x = 2
y = 7
z = True
print(x, y, z)

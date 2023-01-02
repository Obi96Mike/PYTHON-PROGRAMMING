# Operator - symbol that indicates an operator to be performed; +, -, /, *, **, //
# Operand - object that an operator acts on; 2 + 3 are operands while + is operator.

# Standard library of a language are libraries that the language comes with by default e.g Python modules like os, math, threading

# Math module is part of Python standard library and gives many functions e.g., math.sin/cos/tan(x)

# Random module is part of Python standard library and provides many functions that you can use to generate random numbers or make random choices.
# random.randint(start, stop); random.randrange(start, stop, step); random.choice(iterable)

# Bitwise operators

# STANDARD ARITHMETIC OPERATORS
import math  # Typed on top of program.
import random


print(10 + 3)  # addition
print(10 - 3)  # subtraction
print(10 * 3)  # multiplication
print(10 ** 3)  # exponent
print(10 / 3)  # division
print(10 // 3)  # Integer division; chops off decimal component.
# If negative, rounds off to nearest number; divides and rounds to the nearest integer.
print(10 % 3)  # modulus; the remainder after dividing one number by another.

# AUGMENTED ASSIGNMENT OPERATORS; PEMDAS
# A shortcut that allows us to reduce total amount of text we need to write; total amount of code we need to print whenever we have a variable and we want to do something with its current value and then take the new value and assign it back to original variable.
x = 10
x = x + 3
x += 3
print(x)

a = 1
a += 2
print(a)

b = 5
b *= 3
print(b)

c = 3
c -= 2
print(c)

d = 6
d /= 2
print(d)


# MULTIPLE VARIABLE ASSIGNMENTS
a = b = 5
a, b = 5, 10  # Tuples

# WORKING WITH NUMBERS
# Python3 Module - mathematical functions for working with numbers.
# Use dot notation to see all methods available in the object class
print(round(2.9))
print(abs(-2.9))
print(math.floor(-3.14))


# MATH MODULE
# max and min function; gives maximum value and minimum value inside of an iterable object.
x = max([1, 2, 5])
print(x)

y = max("a", "b")
print(y)

# sum function; gives sum of all arguments or of any iterable object.
x = sum([3.4, 5.6])  # List
print(x)

x = sum((-4, 1, 2, 3))
print(x)

x = round(3.49, 2)
print(x)

x = math.cos(90)
print(x)


# RANDOM MODULE allows us to randomly select things or generate random numbers.
random_number = random.randint(1, 10)  # returns random int in range [a, b]
print(random_number)

random_number = random.randrange(1, 10, 2)
print(random_number)

lst = ['he', 'hi', 'ho']
# randomly selects something from an iterable.
random_number = random.choice(lst)
print(random_number)


# Assign and Modify Variables
# Note that this code uses scientific notation to define large numbers. 4.445e8 is equal to 4.445 * 10 ** 8 which is equal to 444500000.0.
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall *= .9

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume *= 1.05

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5

# print the new value of the reservoir_volume variable
print(reservoir_volume)

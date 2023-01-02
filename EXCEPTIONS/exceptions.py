# In general, there are two types of errors to look out for:
# Exceptions
# Syntax or Parsing errors

# An Exception is a problem that occurs when the code is running, but a 'Syntax Error' is a problem detected when Python checks the code before it runs it.


# When writing programs, they may encounter errors and terminate because of programmer's mistakes, bad data from user, resources nit being available.
# An exception is an object to report an error while our program is running; errors raised in our program when we do something invalid.
# EXCEPTION HANDLING is code that handles errors, code that runs when a program does not go as planned.
# An exception is an error that occurs during the execution of a program; it is a special object type that Python uses to manage errors during program execution; it is an error that terminates the execution of a program.
# A traceback is a report of the exception that was raised.


# timeit module calculates execution time of some Python code.
from timeit import timeit
from timeit import timeit  # timeit module
numbers = [1, 2]
# print(numbers[3]) IndexError:list index out of range; an exception.

age = int(input("Enter Age: "))
# In Terminal, if user inputs value a non-numeric value like a, you get an exception; program crashes. One gets an exception of type ValueError.


# HANDLING EXCEPTIONS
# try-except block
# When Python sees a try block, it executes every statement in this block.
try:  # try block; An except or finally block is required and must come after the try. You can have multiple except blocks after a single try.
    age = int(input("Age: "))
# except clause is executed incase of an exception or error in the try block.
except ValueError as ex:  # One can optionally add a variable that will include details about the exception; mostly the error message, and sometimes additional arguments.
    print("You didn't enter a valid age")
    print(ex)
    print(type(ex))
else:  # else clause executed if no exceptions is known in the code we add on the try block. else clause executed if we have no exceptions.
    print("No exceptions were thrown.")
print("Execution continues.")


try:
    age = int(input("Age: "))
    xfactor = 10 / age  # You can't divide a number by 0 in programming.
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")


try:
    i = int("hello")
# Any exception will run. Not a good pracice to accept a general exception.
except Exception as e:
    print(f"Caught the exception: {e}")


try:
    2/0
except ZeroDivisionError as e:
    print("Zero Div Exception!", e)


def divide_five_by_number(n):
    try:
        calculation = 5 / n
    except:  # except : pass
        calculation = 5
    return calculation


print(divide_five_by_number(0))
print(divide_five_by_number(10))
print(divide_five_by_number("Nonsense"))

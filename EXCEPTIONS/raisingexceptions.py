# RAISING EXCEPTIONS
# Use raise keyword then define what error you want to raise (to create an exception/error in Python). In many other programming languages, you "throw" an exception or error. In Python, however, you "raise" them.
# Python 3 built-in exceptions
raise ValueError("This is an error!")
raise Exception("This is an error!")  # raising general exceptions.

# raising an exception when user inputs an invalid number.
num = input("Enter a number: ")
if not num.isdigit():
    raise ValueError("This is not a valid number.")


while True:
    num = input("Enter a number: ")
    try:
        num = float(num)
        break
    except ValueError:
        print("Not a valid float, try again!")


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('Age cannot be 0 or less.')
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)


# COST OF RAISING EXCEPTIONS
# Runtime and Compile-time exceptions/error

code1 = """
def calculate _xfactor(age):
    if age <= 0:
        raise ValueError('Age cannot be 0 or less.')
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age
xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass 
"""

print("first code=", timeit(code1, number=10000))
print("second code=", timeit(code2, number=10000))

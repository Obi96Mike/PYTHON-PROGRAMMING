# CLEANING UP operations
# finally block to perform clean up operations no matter what try/except block works.
try:
    file = open('exceptions.py')
    age = int(input('Age: '))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Tou didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:  # No matter if there are exceptions or not, the finally block still runs.
    # finally clause releases external resources. It is executed when we have an exception or not, and we use it to release external resources. The perfect place to close files, database connections, network connections.
    file.close()


# WITH STATEMENTS
# shorter and cleaner way to achieve finally clause.
# Works with certain kind of objects.
try:
    with open('app.py') as file:
        print('File opened.')
    age = int(input('Age: '))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Tou didn't enter a valid age.")
else:
    print("No exceptions were thrown.")

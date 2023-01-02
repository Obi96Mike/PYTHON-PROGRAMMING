numbers = [1, 2]
# When we use the dot notation, we get access to all functions / methods to list objects.
# Every list object in Python has methods e.g., .append, .extend, etc.
# numbers.append() 

# Creating an object like shopping_cart and have methods like add, remove, get_total.
# shopping_cart.add()
# shopping_cart.remove()
# shopping_cart.get_total()

# A point object with methods like draw, move, get_distance to get distance between 2 points
# point.draw()
# point.move()
# point.get_distance()


# Class is a blueprint of creating new objects.
x = 1
# class 'int'> for creating integers. Similarly, we have classes for creating booleans, lists, dictionaries.
print(type(x))
# Every object in Python is created using a class which is a blueprint for creating objects of that type.
# Object - instance of a class.

# Class : Human; define all attributes of humans.
# Objects : Michael, Gilbert, Bella.
# Attributes : eye color, height, weight
# Functions / Methods : walk, talk
 

# CREATING CUSTOM CLASSES
# PascalNamingConvention - first letter of every word should be uppercase, no undercore to separate multiple words.
# Colon to indicate a block.
# Class Name must be singular

# creating a point class in Python
class MyPoint: #PascalCase; then colon to indicate a block of which you'll define all functions related to points.
    def draw(self): # defining all functions related to points e.g drawing/ moving a point.
    # All functions in our classes should have at least 1 parameter, and by convention, we call that parameter self.
    # Optionally, you can add any additional parameters for intializing a point object.
        print("draw")


point = Point(1, 2) # When we create a point object, we want to supply initial values for x and y coordinates.
# To achieve this, we need a constructor which is a special method that is called when we create a new point object.
print(type(point))
print(isinstance(point, Point)) # Wanting to know if an object is an instance of a given class. If point object is an instance of Point class.
print(isinstance(point, int)) # Returns False. point object is not an instance of int class.


class Person():
    pass


obi = Person()
mike = Person()


class DatabaseConnection():
    pass


# Classes allow us to logically group data and functions (attributes and methods)
# Methods are functions associated with a class. They all take in instance self. 
# Each employee is going to have a name, an email address, a pay, and also actions that they can perform. 
# Instance variables contain variables that is unique to each instance; they are set using the self argument in init method.
# init method takes instance self, and first, last name and pay as arguments.

class Employee:
    def __init__ (self, first, last, pay): 
        self.first = first # Instance variable
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self): # method to display employee full name.
        return '{} {}'. format(self.first, self.last)


emp_1 = Employee('Obi', 'Mike', 60000) 
emp_2 = Employee('Test', 'User', 50000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(Employee.fullname(emp_2))

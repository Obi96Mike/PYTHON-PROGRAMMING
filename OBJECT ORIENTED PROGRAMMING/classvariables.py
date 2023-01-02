# Class variables are variables shared among all instances of a class.
# Instance variables are unique for each instance .

class Employee:

    def __init__ (self, first, last, pay): 
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'. format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)

# instance = class()
emp_1 = Employee('Obi', 'Mike', 60000)
emp_2 = Employee('Test', 'User', 50000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)



# A way to write class variables
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__ (self, first, last, pay): 
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1
 
    def fullname(self):
        return '{} {}'. format(self.first, self.last)

    def apply_raise(self):
        # Accessing class variables is through class itself(Employee) or an instance of the class(self.)
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount) 

emp_1 = Employee('Obi', 'Mike', 60000)
emp_2 = Employee('Test', 'User', 50000)

emp_1.raise_amount = 1.05 # changes the raise amount for emp_1
Employee.raise_amount = 1.05 # changes raise_amount for the class and all its instances

print(emp_1.__dict__)
print(Employee.__dict__)


# Accessing class variables from class itself or instance of the class
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emps)




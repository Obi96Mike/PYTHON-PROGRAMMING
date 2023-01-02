class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__ (self, first, last, pay): 
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    # Regular methods in a class take in an instance as the first argument. By convention, it is called self.
    def fullname(self):
        return '{} {}'. format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 

    # Decorator
    @classmethod
    def set_raise_amt(cls, amount): 
        cls.raise_amt = amount


emp_1 = Employee('Obi', 'Mike', 60000)
emp_2 = Employee('Test', 'User', 50000)


Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

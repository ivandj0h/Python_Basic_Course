#Python Class Variable
# In this Python Object-Oriented Tutorial, we will be learning about class variables. We will see how they differ from instance variables and also some ideas for exactly how we would want to use them. Let's get started.

class Employee:

  def __init__(self, first_name, last_name, salary):
    self.first_name = first_name
    self.last_name = last_name
    self.salary = salary
    self.email = first_name + '.' + last_name + '@company.com'

  def full_name(self):
    return '{} {}'.format(self.first_name, self.last_name)

  def salary_rise(self):
    self.salary = int(self.salary * 5)

employee_one = Employee('ivandi', 'djoh', 2500)

# print to the console
print(employee_one.full_name() + ' salary is :')
print(employee_one.salary)
print(employee_one.full_name() + ' salary after added 5% :')
employee_one.salary_rise()
print(employee_one.salary)
# Python Course
# This branch focuses on two built-in functions print() and input() to perform I/O task in Python. Also, you will learn to import modules and use them in your program.

# here is the example using format() :
x = 5
y = 10
print('The value of x is {} and y is {}'.format(x,y))
print()

# other example using format() :
print('I love {0} and {1}'.format('bread','butter'))
print('I love {1} and {0}'.format('bread','butter'))
print()

# We can even use keyword arguments to format the string.
print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))
print()

# To allow flexibility, we might want to take the input from the user. In Python, we have the input() function to allow this. The syntax for input() is:
num = input('Enter a number: ')
print(num)

# When our program grows bigger, it is a good idea to break it into different modules.
import math
print('this is pi number:', math.pi)

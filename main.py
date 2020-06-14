# Python Course

# Namespace
# A namespace is a collection of names.
# In Python, you can imagine a namespace as a mapping of every name you have defined to corresponding objects.
# A namespace containing all the built-in names is created when we start the Python interpreter and exists as long as the interpreter runs.

a = 2
print('id(a) =', id(a))

a = a+1
print('id(a) =', id(a))

print('id(3) =', id(3))

b = 2
print('id(b) =', id(b))
print('id(2) =', id(2))

# Variable Scope
def outer_function():
    a = 70

    def inner_function():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a =', a)
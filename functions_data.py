#variable types

print(type(1))
print(type(0.1))

#variable assigning

#global variables, can be called anywhere!
x = 2
y = 239
print(x + y)

print(type(x))

mylist = [1,2,3,4]

print(type(mylist))

mydictionary = {'cookies': ['oreo', 'oatmeal'], 'cake': ['chocolate', 'pistacio']}

# Integers are just whole numbers, while anything with a decimal is a float
# Modulus '%' is percentages, quotient '//' gives remainder, and exponent is '**'
# Lists and Strings in Python starts on a 0 index, NOT a 1 index

# You can modify the lists, as well as the elements. Even tuples too.

# Booleans! Helpful for comparing all sorts of data sets.
# Make sure your function and variable names are thoughtful so they are easy for peers to follow along to.

def pwr(x,y):
    '''This function raises the first input to the power of the second input.'''
    #local variables, can only be edited and called here, completely different from the outside variables.
    x = 2
    y = 4
    exp = x ** y
    return(exp)

print(pwr(x,y))

# Notebooks like Jupyter can return you what the function does with its description.

a = 24
b = 626

def mult(a,b):
    multiply = a * b
    return(multiply)
print(mult(a,b))
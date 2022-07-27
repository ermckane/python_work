'''
INTERGERS

You can add (+), subtract (-), multiply (*), and divide (/)
integers in Python.
'''

print(2*3)
print(3/2)

#Python uses two multiplication symbols to represent exponents:

print(10**6)

#FLOATS

'''
Python calls any number with a decimal point a float. This
term is used in most programming languages, and it
refers to the fact that a decimal point can appear at any
position in a number. Every programming language must
be carefully designed to properly manage decimal
numbers so numbers behave appropriately no matter
where the decimal point appears.
For the most part, you can use decimals without worrying
about how they behave. Simply enter the numbers you want
to use, and Python will most likely do what you expect:
'''

print(.1+.1)
print(2*.016)
print(.2+.1)

'''
This happens in all languages and is of little concern. Python
tries to find a way to represent the result as precisely as
possible, which is sometimes difficult given how computers
have to represent numbers internally. Just ignore the extra
decimal places for now; you’ll learn ways to deal with the extra
places when you need to in the projects in Part II.
'''

#When you divide any two numbers, even if they are integers 
#that result in a whole number, you’ll always get a float:
print(4/2)

'''
Underscores in Numbers

When you’re writing long numbers, you can group digits
using underscores to make large numbers more readable:
'''

universe_age=14_000_000_000
print(universe_age)

'''
Multiple Assignment

You can assign values to more than one variable using
just a single line. This can help shorten your programs
and make them easier to read; you’ll use this technique
most often when initializing a set of numbers.
For example, here’s how you can initialize the
variables x, y, and z to zero:
'''
x,y,z= 0,1,2
print(x,y,z)

'''
Constants

A constant is like a variable whose value stays the same
throughout the life of a program. Python doesn’t have
built-in constant types, but Python programmers use all
capital letters to indicate a variable should be treated as a
constant and never be changed:
'''

MAX_CONNECTIONS=5000

'''
A list is a collection of items in a particular order. Since 
a list will often contain more than one element,it is a good 
idea for the name of your list to be plural.
'''
fantasies = ['cosmere','red rising','mistborn','dune']
print(fantasies)

'''
Accessing Elements in a List

Lists are ordered collections, so you can access any
element in a list by telling Python the position, or index, of
the item desired. To access an element in a list, write the
name of the list followed by the index of the item enclosed
in square brackets.
'''

print(fantasies[0])

'''
You can also use the string methods from Chapter 2
on any element in this list. For example, you can format
the element 'trek' more neatly by using the title() method:
'''

print(fantasies[0].title())


'''
Index Positions Start at 0, Not 1

Python considers the first item in a list to be at position 0,
not position 1. This is true of most programming
languages, and the reason has to do with how the list
operations are implemented at a lower level. If you’re
receiving unexpected results, determine whether you are
making a simple off-by-one error.

The second item in a list has an index of 1. Using this
counting system, you can get any element you want from a list
by subtracting one from its position in the list. For instance, to
access the fourth item in a list, you request the item at index 3.
The following asks for the fantasies at index 1 and index 3. 
Python has a special syntax for accessing the last
element in a list. By asking for the item at index -1, Python
always returns the last item in the list. This syntax is quite
useful, because you’ll often want to access the last items in a
list without knowing exactly how long the list is. This
convention extends to other negative index values as well.
The index -2 returns the second item from the end of the list,
the index -3 returns the third item from the end, and so forth.:
'''

print(fantasies[1].title())
print(fantasies[2].title())
print(fantasies[-1].title())

'''
Using Individual Values from a List


'''
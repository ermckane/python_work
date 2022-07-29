'''
Sorting a List Permanently with the sort() Method

Often, your lists will be created in an unpredictable order,
because you can’t always control the order in which your
users provide their data. Although this is unavoidable in
most circumstances, you’ll frequently want to present your
information in a particular order. Sometimes you’ll want to
preserve the original order of your list, and other times
you’ll want to change the original order. Python provides a
number of different ways to organize your lists, depending
on the situation.

Python’s sort() method makes it relatively easy to sort a list.
Imagine we have a list of characters and want to change the order of
the list to store them alphabetically. To keep the task simple,
let’s assume that all the values in the list are lowercase.
'''
characters=['Eragorn','Frodo','Bilbo','Gandalf','Sauron']
characters.sort()
print(characters)
'''
The sort() method, shown at ➊, changes the order of the
list permanently. The cars are now in alphabetical order,
and we can never revert to the original order:
You can also sort this list in reverse alphabetical order
by passing the argument reverse=True to the sort() method.
The following example sorts the list of cars in reverse
alphabetical order:
'''
characters.sort(reverse=True)
print(characters)

'''
Sorting a List Temporarily with the sorted() Function

To maintain the original order of a list but present it in a sorted
order, you can use the sorted() function. The sorted() fucntions lets 
you display your list in a particular order but doesnt affect 
the actual order of the list.
'''

characters2=['Eragorn','Frodo','Bilbo','Gandalf','Sauron']
print('\nHere is the original list.')
print(characters2)
print('\nHere is the sorted list.')
print(sorted(characters2))
print('\nHere is the original list.')
print(characters2)

'''
Notice that the list still exists in its original order at ➍
after the sorted() function has been used. The sorted()
function can also accept a reverse=True argument if you want
to display a list in reverse alphabetical order.
'''

'''
Printing a List in Reverse Order

To reverse the original order of a list, you can use the reverse() method. 
If we originally stored the list of characters in chronological
order according to when I first heard of them, we could easily
rearranfe the list into reverse chronological order.The reverse() 
method changes the order of a listpermanently, but you can revert 
to the original orderanytime by applying reverse() to the same list 
a second time.
'''
print(characters2)

characters2.reverse()
print(characters2)

'''
Finding the Length of a List

You can quickly find the length of a list by using the len()
function. The list in this example has five items, so its
length is 5:
'''
print(len(characters))
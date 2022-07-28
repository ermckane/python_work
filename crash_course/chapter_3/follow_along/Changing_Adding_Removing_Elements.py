'''
Most lists you create will be dynamic, meaning youll build a list
and then add and remove elements from it as your program runs
its course. For example, you might create a game in which a player
has to shoot aliens out of the sky. You could store the initial 
set of aliens in a list and then remove an alien from the list
each time one is shot down. Each time an new alien appears on the 
screen, you add it to the list. Your list of aliens will increase 
and decrease in length throughout the course of the game.

Modifying Elements in a List

The syntax fro modifying an element is similar to the syntax for
accessing an element in a list. To change an element, use the name 
of the list followed by the index of the element you want to change,
and then provide the new value you want that item to have.
'''

books=['red rising','stormlight archive','dune','wheel of time']
print(books)

books[0]='mistborn'
print(books[0])

'''
Adding Elements to a List

You might want to add a new element to a list fro many reasons. For 
example, you might want to make new aliens appear in a game, add new
data to a visualization, or add new registered users to a website
you've built. Python provides several ways to add new data to exisiting 
lists.

The simplest way to add a new element to a list is to append the item to
the list. When you appeand an item to a list, the new element is added to 
the end of the list. Using the same list we had in the previous example, we'll
add a new element to the end of the list.
'''

books.append('red rising')
print(books)

'''
Building lists this way is very common, because you
often won’t know the data your users want to store in a
program until after the program is running. To put your
users in control, start by defining an empty list that will
hold the users’ values. Then append each new value
provided to the list you just created.

You can add a new element at any position in your list by using the insert()
method. You do this by specifying the index of the new element and the value 
of the new item.
'''

books.insert(0,'Goblin Emperor')
print(books)

'''
Removing Elements from a List
Often, you’ll want to remove an item or a set of items from a list.
For example, when a player shoots down an alien from the sky,
you’ll most likely want to remove it from the list of active aliens.
Or when a user decides to cancel their account on a web
application you created, you’ll want to remove that user

If you know the position of the item you want to remove from a list,
you can use the del statement.
'''
del books[0]
print(books)

'''
Sometimes you'll want to use the value of an item after you remove it from
a list. For example, you might want to get the x and y position of an alien
that was just shot down, so you can draw an explosion at that position.
In a web application, you might want to remove a user froma list of active
members and then add that user to a list of inactive members.

The pop() mehtod removes the last item in a list, but it lets your work with 
that item after removing it.
'''
popped_books=books.pop()  #If no number is specified, then the default is the last value in the list
print(books)
print(popped_books)
print(f'The books series that I am currently reading is {popped_books.title()}.')

'''
Sometimes you won’t know the position of the value you
want to remove from a list. If you only know the value of the
item you want to remove, you can use the remove() method.
For example, let’s say we want to remove the value
'wheel of time' from the list of books.
'''
books.remove('wheel of time')
books.append('red rising')
print(books)

'''
You can also use the remove() method to work with a value that's being removed
from a list. Let's remove the value red rising and a print a reason for
removing it from the list:
'''
too_long='red rising'
books.remove(too_long)
print(books)
print(f'\nA {too_long.title()} is too long for me.')
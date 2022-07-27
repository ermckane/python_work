# A string is a series of characters. Anything inside quotes is considered a string in Python, and you can use single or double quotes
print("The language 'Python' is named after Monty Python, not the snake.")

#CHANGING CASE IN A STTRING WITH METHODS

name="sir lancelot"
print(name.title())

'''
In this example, the variable name refers to the lowercase
string "ada lovelace". The method title() appears after the variable in
the print() call. A method is an action that Python can perform
on a piece of data. The dot (.) after name in name.title() tells
Python to make the title() method act on the variable name.
Every method is followed by a set of parentheses,
because methods often need additional information to do
their work. That information is provided inside the
parentheses. The title() function doesn’t need any
additional information, so its parentheses are empty.
The title() method changes each word to title case,
where each word begins with a capital letter. This is useful
because you’ll often want to think of a name as a piece of
information. For example, you might want your program to
recognize the input values Ada, ADA, and ada as the same
name, and display all of them as Ada.
Several other useful methods are available for dealing
with case as well. For example, you can change a string
to all uppercase or all lowercase letters like this:
'''

name="Monty Python"
print(name.upper())
print(name.lower())

#USING VARIABLES IN STRINGS

'''
In some situations, you’ll want to use a variable’s value inside a
string. For example, you might want two variables to represent a
first name and a last name respectively, and then want to
combine those values to display someone’s full name:
'''

first_name='ada'
last_name='goldfinger'
full_name=f'{first_name} {last_name}'
print(full_name)

'''
To insert a variable’s value into a string, place the letter
f immediately before the opening quotation mark ➊. Put
braces around the name or names of any variable you
want to use inside the string. Python will replace each
variable with its value when the string is displayed.
These strings are called f-strings. The f is for format,
because Python formats the string by replacing the name
of any variable in braces with its value. You can do a lot with 
f-strings. For example, you canuse f-strings to compose 
complete messages using the information associated with a variable, 
as shown here:
'''

first_name='ada'
last_name='goldfinger'
full_name=f'{first_name} {last_name}'
print(f'Hello, {full_name.title()}!')

'''
Adding Whitespace to Strings with Tabs or Newlines

In programming, whitespace refers to any nonprinting
character, such as spaces, tabs, and end-of-line symbols.
You can use whitespace to organize your output so it’s
easier for users to read.
To add a tab to your text, use the character
combination \t as shown at ➊
'''
print("\tPython")

#To add a newline in a string, use the character combination \n:

print("Languages:\nPython\nC\nSQL")
print("Languages:\n\tPython\n\tC\n\tSQL")

'''
Stripping Whitespace
Extra whitespace can be confusing in your programs. To
programmers 'python' and 'python ' look pretty much the
same. But to a program, they are two different strings.
Python detects the extra space in 'python ' and considers it
significant unless you tell it otherwise.
It’s important to think about whitespace, because often you’ll
want to compare two strings to determine whether they are the
same. For example, one important instance might involve
checking people’s usernames when they log in to a website.
Extra whitespace can be confusing in much simpler situations
as well. Fortunately, Python makes it easy to eliminate
extraneous whitespace from data that people enter.
Python can look for extra whitespace on the right and
left sides of a string. To ensure that no whitespace exists
at the right end of a string, use the rstrip() method.
'''

favorite_language='python '
print(favorite_language.rstrip())

'''
The value associated with favorite_language at ➊ contains
extra whitespace at the end of the string. When you ask
Python for this value in a terminal session, you can see
the space at the end of the value ➋. When the rstrip()
method acts on the variable favorite_language at ➌, this extra
space is removed. However, it is only removed
temporarily. If you ask for the value of favorite_language again,
you can see that the string looks the same as when it was
entered, including the extra whitespace ➍.
To remove the whitespace from the string permanently, you
have to associate the stripped value with the variable name:
'''
favorite_langauge='python '
favorite_languages=favorite_language.rstrip()
print(favorite_languages)

'''
To remove the whitespace from the string, you strip the
whitespace from the right side of the string and then
associate this new value with the original variable, as shown
at ➊. Changing a variable’s value is done often in
programming. This is how a variable’s value can be updated
as a program is executed or in response to user input.
You can also strip whitespace from the left side of a string
using the lstrip() method, or from both sides at once using strip():
'''
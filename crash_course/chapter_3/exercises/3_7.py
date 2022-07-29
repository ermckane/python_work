'''
You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.

Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print a
message to that person letting them know you’re sorry you can’t invite
them to dinner.
Print a message to each of the two people still on your list, letting them
know they’re still invited.
Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
'''
names=['Bert','Ernie','Arthur']
names.insert(0,'Grimace')
names.insert(2,'Ruth')
names.append('Dumbar')
print(names)
message=', you are humbly invited to dinner where you are required to weare a dress, no matter the sex.'
print(f'               \n\
    {names[0]}{message}\n\
    {names[1]}{message}\n\
    {names[2]}{message}\n\
    {names[3]}{message}\n\
    {names[4]}{message}')

print('\n\
    I am sorry to say but my new table has yet to arrive for dinner and I can only invite 2 people.')
uninvited1=names.pop()
uninvited2=names.pop()
uninvited3=names.pop()
cancellation_message=', I am sorry, but for the good of humanity, I have to disinvite you from dinner.'
print(f'                              \n\
    {uninvited1}{cancellation_message}\n\
    {uninvited2}{cancellation_message}\n\
    {uninvited3}{cancellation_message}')
invited_message=', be thankful that I dislike you the least and that I am still inviting you to dine with death.'
print(f'                       \n\
    {names[0]}{invited_message}\n\
    {names[1]}{invited_message}')
del names[0]
del names[0]
print(names)
print(f'{names[0]}, how the hell are you still here? Die you witch!')
del names[0]
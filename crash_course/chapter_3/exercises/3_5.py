'''
You just heard that one of your guests cant make
the dinner, so you need to send out a new set of invitations. Youll have to think
of someone else to invite.
Start with your program from Exercise 3-4. Add a print() call at the end of
your program stating the name of the guest who cant make it.
Modify your list, replacing the name of the guest who cant make it with
the name of the new person you are inviting.
Print a second set of invitation messages, one for each person who is still
in your list.
'''

names=['Jon','Matt','Holden']
names.extend(['Lincoln','Momo'])
print(names)
canceled='Matt'
canceled_name=names.remove('Matt')
print(f'\n\
    {canceled}, you are hereby disinvited do to your associations with Oompa Loompas.')
names.append('Nausica')
print(f'                                                      \n\
    {names[0]}, you are humbly invited to dine at deaths door.\n\
    {names[1]}, you are humbly invited to dine at deaths door.\n\
    {names[2]}, you are humbly invited to dine at deaths door.\n\
    {names[3]}, you are humbly invited to dine at deaths door.\n\
    {names[4]}, you are humbly invited to dine at deaths door.')

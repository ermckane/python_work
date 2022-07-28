'''
You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.

Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
call to the end of your program informing people that you found a bigger
dinner table.
Use insert() to add one new guest to the beginning of your list.
Use insert() to add one new guest to the middle of your list.
Use append() to add one new guest to the end of your list.
Print a new set of invitation messages, one for each person in your lis

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
print("Hello stranger. Please enter a list of your favorite foods one at a time. Once you have no more foods to list, type Done.")

favoriteFoods = []
returnStatement = ''

while True:
    userInput = input('Please enter a food: ')
    if userInput == 'Done':
        break
    transferInput = userInput
    favoriteFoods.append(transferInput)


for x in range(len(favoriteFoods)):
    if returnStatement == '':
        returnStatement = favoriteFoods[x]
    elif x == (len(favoriteFoods)-1):
        returnStatement = f'{returnStatement}, and {favoriteFoods[x]}'
    else:
        returnStatement = f'{returnStatement}, {favoriteFoods[x]}'
print(returnStatement)

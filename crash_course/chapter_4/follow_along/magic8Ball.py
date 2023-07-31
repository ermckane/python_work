magicResponses = ['You suck', 
                  'Please leave me alone',
                  'You have won the lottery',
                  'Suck my toe',
                  'Call me daddy',
                  'JFK comitted suicide. I swear. The slow motion evidence proves it.',
                  'Asparagus sucks',
                  'Game of Thrones is better than Lord the Rings',
                  'Whales should be saved not slaughtered']

while True:
    userInput = input('Please enter a number 1-9:\n')

    try:
        number = int(userInput)
        if number > 9:
            continue
        break
    except ValueError:
        print('You fool, that is not a number')
        continue

print(magicResponses[number])
import random

while True:
    userInput = input()
    
    if len(userInput) > 1:
        continue
    print('Passed phase 1')
    if userInput.isalpha() is True:
        continue
    if int(userInput) in range (1,9):
        print('Passed phase 2')
        break
    break

def getAnswer(answerValue):
    if answerValue == 1:
        return 'It is certain'
    elif answerValue == 2:
        return 'It is decidedly so'
    elif answerValue == 3:
        return 'Yes'
    elif answerValue == 4:
        return 'Reply hazy try again'
    elif answerValue == 5:
        return 'Ask again later'
    elif answerValue == 6:
        return 'Concentrate and ask again later'
    elif answerValue == 7:
        return 'My reply is no'
    elif answerValue == 8:
        return 'Outlook not so good'
    elif answerValue ==9:
        return 'Very doubtful'
   

print(getAnswer(int(userInput)))

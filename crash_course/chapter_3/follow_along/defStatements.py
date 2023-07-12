import random

print('Please enter a number 1 - 9.')

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
    
print(getAnswer(random.randint(1,9)))

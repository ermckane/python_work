def collatz(number):
    
    if number == 1:
        return
    elif number % 2 == 0:
        return number // 2
    else:
        return (number * 3) + 1 
    



while True:

    userInput = input('Please enter a number:\n')

    try:
        number = int(userInput)
        break
    except ValueError:
        print('This is not a number. Please try again.')
        continue
    
print('Starting Collatz Sequence.')
print(f'User input was: {number}')

while (number!= 1):
    number = collatz(number)
    print(number)

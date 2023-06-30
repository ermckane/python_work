print('Please enter your name below:')
name = input()
if name == 'Emry':
    print('Hello, Emry. Please enter password.')
    password = input()
    if password == 'Av@tar':
        print('Access Granted')
    else:
        print('Wrong Password')
else:
    print('Are you human?')
    human = input()
    if human == 'No':
        print('You are not a real person. Say goodbye to your loved ones.')
    elif human == 'Yes':
         print('I will find you imposter.')
    else:
        print('I do not compute.')
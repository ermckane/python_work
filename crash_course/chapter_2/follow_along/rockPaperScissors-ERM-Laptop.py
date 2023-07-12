import random, sys

#These keep track of rounds won, lost, or tied
wins = 0
losses = 0
ties = 0

while True: #Main loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: #Must have player input
        print('Enter our move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quitting the game
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break    
        print('Type one of r, p, s, q.')
    
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    if randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    if randomNumber == 3:
        computerMove = 's'
        print('SCISSORS') 

    if playerMove == computerMove:
        print('It is a tie!')
        ties += 1
    elif playerMove == 'r' and computerMove == 'p':
        print('Computer wins!')
        losses += 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win')
        wins += 1
    elif playerMove == 'p' and computerMove == 's':
        print('Computer wins!')
        losses += 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win')
        wins += 1
    elif playerMove == 's' and computerMove == 'r':
        print('Computer wins!')
        losses += 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win')
        wins += 1
       

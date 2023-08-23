theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print ('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print ('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn

    if theBoard['top-L'] == theBoard['top-M'] and theBoard['top-M'] == theBoard['top-R'] and theBoard['top-L'] == turn:
        print('Team ' + turn + ' wins!')
        break
    elif theBoard['mid-L'] == theBoard['mid-M'] and theBoard['mid-M'] == theBoard['mid-R'] and theBoard['mid-L'] == turn:
        print('Team ' + turn + ' wins!')
        break
    elif theBoard['low-L'] == theBoard['low-M'] and theBoard['low-M'] == theBoard['low-R'] and theBoard['low-L'] == turn:
        print('Team ' + turn + ' wins!')
        break
    elif theBoard['top-L'] == theBoard['mid-L'] and theBoard['mid-L'] == theBoard['low-R'] and theBoard['top-L'] == turn:
        print('Team ' + turn + ' wins!')
        break
    elif theBoard['top-M'] == theBoard['mid-M'] and theBoard['mid-M'] == theBoard['low-M'] and theBoard['top-M'] == turn:
        print('Team ' + turn + ' wins!')
        break
    elif theBoard['top-R'] == theBoard['mid-R'] and theBoard['mid-R'] == theBoard['low-R'] and theBoard['top-R'] == turn:
        print('Team ' + turn + ' wins!')
        break
    elif theBoard['top-L'] == theBoard['mid-M'] and theBoard['mid-M'] == theBoard['low-R'] and theBoard['top-L'] == turn:
        print('Team ' + turn + ' wins!')
        break
    elif theBoard['top-R'] == theBoard['mid-M'] and theBoard['mid-M'] == theBoard['low-L'] and theBoard['top-R'] == turn:
        print('Team ' + turn + ' wins!')
        break

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)

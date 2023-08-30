"""In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen',
'2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board.
Write a function named isValidChessBoard() that takes a dictionary argument
and returns True or False depending on if the board is valid.
A valid board will have exactly one black king and exactly one white
king. Each player can only have at most 16 pieces, at most 8 pawns, and
all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t
be on space '9z'. The piece names begin with either a 'w' or 'b' to represent
white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or
'king'. This function should detect when a bug has resulted in an improper
chess board."""

import random

#Giving each side their pieces
pieceValue = 0
pieces = ('rook', 'knight', 'bishop', 'king', 'queen'
          , 'bishop', 'rook', 'knight', 'pawn', 'pawn', 
          'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', )
whitePieces = []
blackPieces = []

for x in pieces:
    whitePieces.append('w' + pieces[pieceValue])
    blackPieces.append('b' + pieces[pieceValue])
    pieceValue += 1

#Check to make sure previous code worked
print(whitePieces)
print(blackPieces)

#Create chess board   
xValue = 1
chessBoard = {}
yValues = ['a','b','c','d','e','f','g','h']
                                                                                                                                 
for x in range(8):
    yValue = 0
    for y in range(8):
        if xValue <= 2:
            chessBoard.setdefault(str(xValue) + yValues[yValue], whitePieces.pop(0))
        elif xValue >= 7:
            chessBoard.setdefault(str(xValue) + yValues[yValue], blackPieces.pop(len(blackPieces) -1))
        else:
            chessBoard.setdefault(str(xValue) + yValues[yValue], '')
        yValue += 1
    xValue += 1

print(chessBoard)

#Populating chess board with pieces




#def isValidChessBoard():

  
           


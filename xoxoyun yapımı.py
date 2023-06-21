#xox oyun yapalım


theBoard2 = {'1': '','2': '','3': '',
            '4': '','5': '','6': '',
            '7': '','8': '','9': '',}


theBoard = {'1': '1','2': '2','3': '3',
            '4': '4','5': '5','6': '6',
            '7': '7','8': '8','9': '9',}


def  printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'] + '|')
    print(board['4'] + '|' + board['5'] + '|' + board['6'] + '|')
    print(board['7'] + '|' + board['8'] + '|' + board['9'] + '|')

turn ='X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn +' hangisini oynatcaksın ')
    
    oynat = input()
    theBoard[oynat] = turn
    if turn == "X":
        turn = 'O'
    else:
        turn = 'X'
def  printBoard2(board):
    print(board[''] + '|' + board[''] + '|' + board[''] + '|')
    print(board[''] + '|' + board[''] + '|' + board[''] + '|')
    print(board[''] + '|' + board[''] + '|' + board[''] + '|')

turn ='X'
for i in range(9):
    printBoard2(theBoard)
    print('Turn for ' + turn +' hangisini oynatcaksın ')
    
    oynat = input()
    theBoard2[oynat] = turn
    if turn == "X":
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)
printBoard2(theBoard2)

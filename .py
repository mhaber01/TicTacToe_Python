# Solution for Assignment 8 - Tic Tac Toe Game
# By Megan Haber

def drawboard(board):
    for row in board:
        for col in row:
            print(col,end=" ")
        print()

def getcell(board):
    row = int(input('Enter row.'))
    col = int(input('Enter column.'))
    while ((row>2 or row<0 or col>2 or col<0)or(board[row][col]=='O' or board[row][col]=='X')):
        row = int(input('Enter row.'))
        col = int(input('Enter column.'))
    return row, col

def updateboard(row,col,symbol,board):
    if symbol==1:
        board[row][col]='X'
        return board
    if symbol==2:
        board[row][col]='O'
        return board

def checkwin(board):
    #checks if move was on vertical line and causes win
    if board[0][0]=='X' and board[1][0]=='X'and board[2][0]=='X':
        return True
    elif board[0][0]=='O' and board[1][0]=='O' and board[2][0]=='O':
        return True
    elif board[0][1]=='X' and board[1][1]=='X' and board[2][1]=='X':
        return True
    elif board[0][1]=='O' and board[1][1]=='O' and board[2][1]=='O':
        return True
    elif board[0][2]=='X' and board[1][2]=='X' and board[2][2]=='X':
        return True
    elif board[0][2]=='X' and board[1][2]=='X' and board[2][2]=='X':
        return True
    #checks if move was on horizontal line and causes win
    elif board[0][0]=='X' and board[0][1]=='X' and board[0][2]=='X':
        return True
    elif board[0][0]=='O' and board[0][1]=='O' and board[0][2]=='O':
        return True
    elif board[1][0]=='X' and board[1][1]=='X' and board[1][2]=='X':
        return True
    elif board[1][0]=='O' and board[1][1]=='O' and board[1][2]=='O':
        return True
    elif board[2][0]=='X' and board[2][1]=='X' and board[2][2]=='X':
        return True
    elif board[2][0]=='O' and board[2][1]=='O' and board[2][2]=='O':
        return True
    #checks if move was on first diagonal and causes win
    elif board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X':
        return True
    elif board[0][0]=='O' and board[1][1]=='O' and board[2][2]=='O':
        return True
    #checks if move was on second diagonal and causes win
    elif board[0][2]=='X' and board[1][1]=='X' and board[2][0]=='X':
        return True
    elif board[0][2]=='O' and board[1][1]=='O' and board[2][0]=='O':
        return True
    return False

def checktie(board):
    if '-' not in board[0] and '-' not in board[1] and '-' not in board[2]:
        return True
    else:
        False
        
def startgame():
    print('Tic Tac Toe')
    p1 = str(input('Welcome Player X!  Please enter your name.'))
    p2 = str(input('Welcome Player O!  Please enter your name.'))
    myboard = [['-','-','-'],['-','-','-'],['-','-','-']]
    drawboard(myboard)
    while True:
        print(p1 + "'s turn.")
        cell = getcell(myboard)
        turn = 1
        updateboard(cell[0],cell[1],turn,myboard)
        checkwin(myboard)
        checktie(myboard)
        drawboard(myboard)
        if checkwin(myboard)==True and turn==1:
            print('Congratulations, ' + p1 + ', you win!')
            break
        if checktie(myboard)==True:
            print("It's a tie!")
            break
        print(p2 + "'s turn.")
        cell = getcell(myboard)
        turn = 2
        updateboard(cell[0],cell[1],turn,myboard)
        checkwin(myboard)
        checktie(myboard)
        drawboard(myboard)
        if checkwin(myboard)==True and turn==2:
            print('Congratulations, ' + p2 + ', you win!')
            break
        if checktie(myboard)==True:
            print("It's a tie!")
            break

print(startgame())

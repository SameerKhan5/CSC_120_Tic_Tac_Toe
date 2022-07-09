board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]
player = 1

def printBoard():
    global board
    for row in board:
        print(row)

def checkMark(row, column):
    global board
    if (board[row-1][column-1] != '-'):
        return True
    else:
        return False

def placeMark(row, column):
    global board, player
    if (player == 1):
        board[row-1][column-1] = "X"
    else:
        board[row-1][column-1] = "O"

def game():
    printBoard()
    turn()
    game()

def turn():
    global player
    invalid = True
    while invalid:
        print("Player " + str(player) + "'s turn")
        row = int(input("Row: "))
        column = int(input("Column: "))
        invalid = checkMark(row, column)
    placeMark(row, column)
    player = 1 if player == 2 else 2
    
game()
    



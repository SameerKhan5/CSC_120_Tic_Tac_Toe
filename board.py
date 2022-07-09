board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]
player = 1
winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

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

def turn():
    global player
    invalid = True
    while invalid:
        print("Player " + str(player) + "'s turn")
        row = int(input("Row: "))
        column = int(input("Column: "))
        invalid = checkMark(row, column)
    placeMark(row, column)

def checkWin():
    global player, board
    won = False
    newBoard = []
    for i in range(0,len(board)):
        for j in range(0,len(board)):
            newBoard += [board[i][j]]
    for i in range(0, 7):
        winningCondition = winningConditions[i]
        first = newBoard[winningCondition[0]]
        second = newBoard[winningCondition[1]]
        third = newBoard[winningCondition[2]]
        if (first == '-' or second == '-' or third == '-'):
            continue
        if (first == second and second == third):
            won = True
            break
    if (won == True):
        if (player == 1):
            print("Player 1 won")
            print("Player 2 lost")
        else:
            print("Player 2 won")
            print("Player 1 lost")
    elif(not("-" in "".join(newBoard))):
        print("Draw")
    else:
        player = 1 if player == 2 else 2
        game()

def game():
    printBoard()
    turn()
    checkWin()

game()


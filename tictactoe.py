#imports
import random

#create the game board and initilize variables
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

curplyr = 'x'
winner = None
rungame = True

def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#player input
def playerinput(board):
    play = int(input("Select a spot 1-9: "))
    if board[play-1] == "-":
        board[play-1] = curplyr.capitalize()
    else:
        print("you can't play there")

#check for win or tie
def checkrow(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkcolumn(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True
        
def checkdiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True

def checkIfWin(board):
    global rungame
    if checkcolumn(board):
        printboard(board)
        print(f"The winner is {winner}!")
        rungame = False

    elif checkrow(board):
        printboard(board)
        print(f"The winner is {winner}!")
        rungame = False

    elif checkdiag(board):
        printboard(board)
        print(f"The winner is {winner}!")
        rungame = False

def checkIfTie(board):
    global rungame
    if "-" not in board:
        printboard(board)
        print("It is a tie!")
        rungame = False

# switch player
def switchplyr():
    global curplyr
    if curplyr.capitalize() == "X":
        curplyr = "O"
    else:
        curplyr = "X"

#npc
def computer(board):
    while curplyr == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchplyr()

#main function
def main():
    plys = input('one or two player?: ')
    if plys.upper() == 'ONE' or plys == '1':
        while rungame:
            printboard(board)
            playerinput(board)
            switchplyr()
            computer(board)
            checkIfWin(board)
            checkIfTie(board)
    elif plys.upper() == 'TWO' or plys == '2':
        while rungame:
            printboard(board)
            playerinput(board)
            switchplyr()
            checkIfWin(board)
            checkIfTie(board)

if __name__ == '__main__':
    main()
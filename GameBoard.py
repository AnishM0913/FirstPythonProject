# Author: Anish Menghani

import sys
import random


board = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9']]


# main method
def main(board):

    numX = 0
    numO = 0
    while VictoryFor(board, 'X') is False and VictoryFor(board, 'O') is False:

        if numX >= numO:
            VictoryFor(board, 'O')
            EnterMove(board)
            numO += 1

        elif numO > numX:
            VictoryFor(board, 'X')
            drawMove(board)
            numX += 1


# Displays the Game board along with values of each cell
def DisplayBoard(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def ListOfTakenFields(board):
    invalidvals = []
    for i in range(len(board)):
        for f in range(len(board)):
            if board[i][f] == 'O':
                invalidvals.append((i, f))
            elif board[i][f] == 'X':
                invalidvals.append((i, f))
            elif board[i][f] != 'O':
                continue
    return invalidvals


# Makes list of free spaces in the board
def MakeListOfFreeFields(board):

    validVals = []

    for i in range(len(board)):
        for f in range(len(board)):
            if board[i][f] == 'O':
                continue
            elif board[i][f] == 'X':
                continue
            elif board[i][f] != 'O':
                validVals.append((i, f))

    return validVals


# User Enters Code
def EnterMove(board):

    move = int(input("Enter your move: "))

    if int(move) > 9 or move < 1:
        print("invalid input, please enter a valid number between 1 and 9: ")
        EnterMove(board)

    move -= 1
    row = move // 3
    col = move % 3

    if board[row][col] == 'O' or board[row][col] == 'X':
        print("Space has been taken")
        EnterMove(board)

    elif board[row][col] == str(move+1):
        board[row][col] = 'O'
        DisplayBoard(board)


def VictoryFor(board, sign):
    sign = str(sign)

    for i in range(len(board)):

        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            print(sign + "wins", sep=' ')
            return True

        elif board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            print(sign + "wins", sep=' ')
            return True

        elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
            print(sign + "wins", sep=' ')
            return True

        elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
            print(sign + "wins", sep=' ')
            return True

    return False


def drawMove(board):

    lst = MakeListOfFreeFields(board)
    num1 = random.randrange(len(lst))

    ranchoice = lst[num1]

    board[ranchoice[0]][ranchoice[1]] = 'X'
    DisplayBoard(board)


main(board)

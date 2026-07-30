# TicTocToe 3x3
# Player use 'X', AI use 'O' and AI cannot lose (means can just win or draw)
# Minimax algorithm
# 0 | 1 | 2
# 3 | 4 | 5
# 6 | 7 | 8
import math
board = [' ' for _ in range(9)]
def printBoard():
    for i in range(3):
        print(board[i*3] + ' | ' + board[i*3+1] + ' | ' + board[i*3+2])

def checkWin(board):
    winConditions = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6]           # diagonals
    ]
    for condition in winConditions:
        # 3 blocks is the same and not empty
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]

    return None
def checkDraw(board):
    if ' ' not in board and checkWin(board) is None:
        return 1
    return 0
# depth: numbers of visited blocks, turn = 1 for AI, turn = 0 for player
def minimax(board, depth, turn):
    #End game
    winner = checkWin(board)
    if winner == 'O': return 1
    if winner == 'X': return -1
    if checkDraw(board) == 1: return 0
    # AI turn
    if turn == 1:
        bestScore = -math.inf
        # Need the max score for AI
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O' #AI trial move
                score = minimax(board, depth + 1, 0)
                board[i] = ' ' #Undo trial move
                bestScore = max(score, bestScore)
        return bestScore
    # Player turn (AI try to minimize the score)
    else:
        # Need the min score for player
        bestScore = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X' #Player trial move
                score = minimax(board, depth + 1, 1)
                board[i] = ' ' #Undo trial move
                bestScore = min(score, bestScore)
        return bestScore
def AI_move(board):
    bestScore = -math.inf
    savedMove = 0 # Save the best move for AI
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O' #AI trial move
            score = minimax(board, 0, 0)
            board[i] = ' ' #Undo trial move
            if score > bestScore:
                bestScore = score
                savedMove = i
    board[savedMove] = 'O'
def play_time():
    print("Play Tic-Tac-Toe with AI | You are 'X', AI is 'O'.")
    print("Sample Board:")
    print("0 | 1 | 2")
    print("3 | 4 | 5")
    print("6 | 7 | 8")
    print("Our Board:")
    printBoard()
    while 1:
        move = int(input("Choose position (0->8): "))
        if board[move] == ' ':
            board[move] = 'X'
        else:
            print("This square has already been played")
            continue
        if checkWin(board) == 'X':
            printBoard()
            print("Good game, you win!")
            break
        elif checkDraw(board):
            printBoard()
            print("Draw")
            break
        # AI turn
        AI_move(board)
        print("\n AI has already move: ")
        printBoard()
        if checkWin(board) == 'O':
            print("AI win! Nice try")
            break
        elif checkDraw(board):
            print("Draw")
            break

if __name__ == '__main__':
    play_time()

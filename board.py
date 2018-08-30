import random
class Intro:
    print('Welcome to Tic Tac Toe!')
    print("This is the game board")
    print('1' + ' | ' + '2' + ' | ' + '3')
    print('-----------')
    print('4' + ' | ' + '5' + ' | ' + '6')
    print('-----------')
    print('7' + ' | ' + '8' + ' | ' + '9')
    print('')
def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'player1'
    else:
        return 'player2'

def inputPlayerLetter():
    # Lets player1 choose which letter they want to be.
    # Returns a list with player1's letter as the first item, and the player 2's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print(player1+ ', do you want to be X or O?')
        letter = input().upper()

    # the first element in the tuple is player1's letter, the second is player 2's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayer1Move(board):
    # Let player1 type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print(player1+ ', what is your next move? (1-9)')
        move = input()
    return int(move)

def getPlayer2Move(board):
    # Let the player2 type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print(player2+ ', what is your next move? (1-9)')
        move = input()
    return int(move)


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Player 1, enter your name')
player1 = input()
print('Who are you playing against ' + player1+ '?')
player2 = input()

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1Letter, player2Letter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(turn+ ' will go first.')
    gameIsPlaying = True\

    while gameIsPlaying:
        if turn == 'player1':
            # Player 1's turn.
            drawBoard(theBoard)
            move = getPlayer1Move(theBoard)
            makeMove(theBoard, player1Letter, move)

            if isWinner(theBoard, player1Letter):
                drawBoard(theBoard)
                print(player1+' has won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('It\'s a tie')
                    break
                else:
                    turn = 'player2'

        else:
            # Player 2's turn.
            drawBoard(theBoard)
            move = getPlayer2Move(theBoard)
            makeMove(theBoard, player2Letter, move)

            if isWinner(theBoard, player2Letter):
                drawBoard(theBoard)
                print(player2+' has won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('It\'s a tie')
                    break
                else:
                    turn = 'player1'

    if not playAgain():
        break
      
   
        

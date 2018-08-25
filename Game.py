import board, player,random
def whoGoesFirst(a, b):
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return a
    else:
        return b

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('Welcome to Tic Tac Toe!')
myboard = board.Board()
print("ENTER PLAYER 1'S NAME.")
nameA = input()
print("ENTER PLAYER 2'S NAME.")
nameB = input()
playerA = player.Player(nameA, "A")
playerB = player.Player(nameB, "B")
while True:
    # Reset the myboard
    myboard.reset()
    turn = whoGoesFirst(playerA, playerB)
    print(turn.getName() + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == playerA:
            # Player's turn.
            myboard.drawBoard()
            move = ' '
            while str(move) not in '1 2 3 4 5 6 7 8 9'.split() or not myboard.isSpaceFree(int(move)):
                move = playerA.getPlayerMove()
            myboard.makeMove(playerA.getLetter(), move)

            if myboard.isWinner(playerA.getLetter()):
                myboard.drawBoard()
                print('You win.')
                gameIsPlaying = False
            else:
                if myboard.isBoardFull():
                    myboard.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = playerB

        else:
            # Player B's turn.
            myboard.drawBoard()
            move = ' '
            while str(move) not in '1 2 3 4 5 6 7 8 9'.split() or not myboard.isSpaceFree(int(move)):
                move = playerB.getPlayerMove()
            myboard.makeMove(playerB.getLetter(), move)

            if myboard.isWinner(playerB.getLetter()):
                myboard.drawBoard()
                print('You win.')
                gameIsPlaying = False
            else:
                if myboard.isBoardFull():
                    myboard.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = playerA

    if not playAgain():
        break
import Board, Player,random
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
board = Board()
print("ENTER PLAYER 1'S NAME.")
nameA = input()
print("ENTER PLAYER 2'S NAME.")
nameB = input()
playerA = Player(nameA, "A")
playerB = Player(nameB, "B")
while True:
    # Reset the board
    turn = whoGoesFirst(playerA, playerB)
    print(turn.getName() + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == playerA:
            # Player's turn.
            board.drawBoard()
            move = playerA.getPlayerMove()
            board.makeMove(playerA.getLetter(), move)

            if board.isWinner(playerA.getLetter()):
                board.drawBoard()
                print('Hooray!' + playerA.getName()+ ' has won the game!')
                gameIsPlaying = False
            else:
                if board.isBoardFull():
                    board.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = playerB

        else:
            # Player B's turn.
            move = playerB.getPlayerMove()
            board.makeMove(playerB.getLetter(), move)

            if board.isWinner(playerB.getLetter()):
                board.drawBoard()
                print(playerA.getName() + 'has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if board.isBoardFull():
                    board.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = playerA

    if not playAgain():
        break
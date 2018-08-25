class Player:
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter
    def getPlayerMove(self):
        # Let the player type in his move.
        print('What is your next move? (1-9)')
        move = input()
        return int(move)
    def getName(self):
        return self.name;
    def getLetter(self):
        return self.letter;

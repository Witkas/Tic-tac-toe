import random
import time

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # Choose random available spot on the board
        return random.choice(game.get_available_spots())

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # User input
        choice = int(input("Select a square (1-9): "))
        return choice - 1
    
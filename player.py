import random
import time

class Player:
    def __init__(self, letter):
        self.letter = letter

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # User input
        choice = int(input("Select a square (1-9): "))
        return choice - 1

class ComputerPlayer(Player):
    pass

class RandomComputerPlayer(ComputerPlayer): 
    def get_move(self, game):
        # Choose random available spot on the board
        return random.choice(game.get_available_spots())

class GeniusComputerPlayer(ComputerPlayer):
    pass

    
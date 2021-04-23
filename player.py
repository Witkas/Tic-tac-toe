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
        try:
            choice = int(input("Select a square (1-9): ")) - 1
            if not game.is_valid_move(choice):
                raise ValueError
            return choice
        except ValueError:
            print("Invalid move. Please try again.")
            return self.get_move(game)

class ComputerPlayer(Player):
    pass

class RandomComputerPlayer(ComputerPlayer): 
    def get_move(self, game):
        # A brief pause
        print("Computer is making a move...")
        time.sleep(0.5)
        # Choose random available spot on the board
        return random.choice(game.get_available_spots())

class GeniusComputerPlayer(ComputerPlayer):
    pass

    
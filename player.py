import random
import time
import math

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
    def get_move(self, game):
        # A brief pause before modifying the board
        print("Computer is making a move...")
        time.sleep(0.3)

class RandomComputerPlayer(ComputerPlayer): 
    def get_move(self, game):
        super().get_move(game)
        # Choose random spot on the board
        return random.choice(game.get_available_spots())

class GeniusComputerPlayer(ComputerPlayer):
    def __init__(self, letter):
        super().__init__(letter)
        self.current_letter = self.letter # Used for simulating future games
    def get_move(self, game):
        super().get_move(game)
        if len(game.get_available_spots()) == 9:
            # Choose random spot on the board
            return random.choice(game.get_available_spots())
        else:
            return self.minimax(game, self)["position"]
            
    def minimax(self, game, current_player):
        # The computer will choose the best possible spot using the minimax algorithm.
        # I implement this algorithm using the following formula:
        # game_state * (empty_spots + 1)
        # where game_state can be either win (1), loss (-1) or tie (0)
        # and empty_spots is the count of empty spots left on the board.
        #
        # The computer will check all of the possibilities of moves in the game, and will choose the move
        # for which the formula results with the highest value.
        # This way, it always maximizes the gains and minimizes any loss, assuming that the opponent 
        # makes the smartest possible move.
        #
        # With this strategy, it is impossible to defeat GeniusComputerPlayer.

        def get_game_state(game):
            winner = game.get_winner()
            if winner != None:
                if winner == self:
                    return 1    # Computer wins
                else:
                    return -1   # Opponent wins
            elif game.is_board_full():
                return 0        # Tie
            else:
                return None # Game not finished yet

        # Base case: game is finished either by win, loss or tie.
        game_state = get_game_state(game)
        if game_state != None:
            return {
                "position": None,
                "score": game_state * (len(game.get_available_spots()) + 1)
            }
        
        if self.current_letter == self.letter:
            best = {
                "position": None,
                "score": -math.inf  # We want to maximize the potential of our move
            }
        else:
            best = {
                "position": None,
                "score": math.inf   # The opponent wants to minimize the potential of their move
            }

        for possible_move in game.get_available_spots():
            # 1. Modify the board
            game.board[possible_move] = self.current_letter
            # 2. Simulate the game using recursion
            self.current_letter = "O" if self.current_letter == "X" else "X"
            simulated_score = self.minimax(game, self)
            self.current_letter = "O" if self.current_letter == "X" else "X"
            # 3. Undo the move
            game.board[possible_move] = " "
            game.current_winner = None
            simulated_score["position"] = possible_move
            # 4. Choose the best possible move
            if self.current_letter == self.letter and simulated_score["score"] > best["score"]:
                best = simulated_score
            elif self.current_letter != self.letter and simulated_score["score"] < best["score"]:
                best = simulated_score
        return best

class IdiotComputerPlayer(ComputerPlayer):
    # Funny reversal of the logic behind the GeniusComputerPlayer.
    # This player will try to lose deliberately.
    def __init__(self, letter):
        super().__init__(letter)
        self.current_letter = self.letter # Used for simulating future games
    def get_move(self, game):
        super().get_move(game)
        if len(game.get_available_spots()) == 9:
            # Choose random spot on the board
            return random.choice(game.get_available_spots())
        else:
            return self.minimax(game, self)["position"]
            
    def minimax(self, game, current_player):
        def get_game_state(game):
            winner = game.get_winner()
            if winner != None:
                if winner == self:
                    return 1    # Computer wins
                else:
                    return -1   # Opponent wins
            elif game.is_board_full():
                return 0        # Tie
            else:
                return None # Game not finished yet

        # Base case: game is finished either by win, loss or tie.
        game_state = get_game_state(game)
        if game_state != None:
            return {
                "position": None,
                "score": game_state * (len(game.get_available_spots()) + 1)
            }
        
        if self.current_letter == self.letter:
            best = {
                "position": None,
                "score": math.inf  # We want to minimize the potential of our move
            }
        else:
            best = {
                "position": None,
                "score": -math.inf   # The opponent wants to maximize the potential of their move
            }

        for possible_move in game.get_available_spots():
            # 1. Modify the board
            game.board[possible_move] = self.current_letter
            # 2. Simulate the game using recursion
            self.current_letter = "O" if self.current_letter == "X" else "X"
            simulated_score = self.minimax(game, self)
            self.current_letter = "O" if self.current_letter == "X" else "X"
            # 3. Undo the move
            game.board[possible_move] = " "
            game.current_winner = None
            simulated_score["position"] = possible_move
            # 4. Choose the WORST possible move
            if self.current_letter == self.letter and simulated_score["score"] < best["score"]:
                best = simulated_score
            elif self.current_letter != self.letter and simulated_score["score"] > best["score"]:
                best = simulated_score
        return best      
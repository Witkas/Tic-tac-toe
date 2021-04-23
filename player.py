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
    pass

class RandomComputerPlayer(ComputerPlayer): 
    def get_move(self, game):
        # A brief pause before modifying the board
        print("Computer is making a move...")
        time.sleep(0.5)
        # Choose random spot on the board
        return random.choice(game.get_available_spots())

class GeniusComputerPlayer(ComputerPlayer):
    def __init__(self, letter):
        super().__init__(letter)
        self.letter_copy = self.letter # Copy for comparison
    def get_move(self, game):
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
            #game.print_board(game.board)
            #print("winner = " + str(winner))
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
        
        if self.letter == self.letter_copy:
            best = {
                "position": None,
                "score": -math.inf  # We want to maximize the potential of our move
            }
        else:
            best = {
                "position": None,
                "score": math.inf   # The opponent will want to minimize the potential of their move
            }

        for possible_move in game.get_available_spots():
            # 1. Modify the board
            game.board[possible_move] = self.letter
            #game.print_board(game.board)
            # 2. Simulate the game using recursion
            #print("swap 1")
            self.letter = "O" if self.letter == "X" else "X"
            simulated_score = self.minimax(game, self)
            #print("swap 2")
            self.letter = "O" if self.letter == "X" else "X"
            # 3. Undo move
            game.board[possible_move] = " "
            game.current_winner = None
            simulated_score["position"] = possible_move
            # 4. Choose the best possible move
            #print(f"Comparing {simulated_score['score']} and {best['score']} while {self.letter}")
            if self.letter == self.letter_copy and simulated_score["score"] > best["score"]:
                best = simulated_score
            elif self.letter != self.letter_copy and simulated_score["score"] < best["score"]:
                best = simulated_score
            
            #game.print_board(game.board)
            #print("score = " + str(best["score"]))
            #print("self.letter = " + self.letter)
        #print(self.letter)
        #print(self.letter_copy)
        #self.letter = self.letter_copy
        return best      
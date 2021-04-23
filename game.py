from player import *

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self, board):
        grouped_board = [board[i*3:(i+1)*3] for i in range(3)]  # E.g. [1,2,3,4,5,6,7,8,9] --> [[1,2,3],[4,5,6],[7,8,9]]
        for group in grouped_board:
            print("| " + " | ".join(group) + " |")  # Prints each row

    def print_board_indices(self):
        # Prints the arrangement of the indices on the board (used at the beginning of the game).
        indices = [str(i) for i in range(1,10)]
        self.print_board(indices)
    
    def is_won(self):
        # Check rows
        rows = [self.board[i*3:(i+1)*3] for i in range(3)]  # E.g. [1,2,3,4,5,6,7,8,9] --> [[1,2,3],[4,5,6],[7,8,9]]
        for row in rows:
            if all(spot == "X" for spot in row) or all(spot == "O" for spot in row):
                return True
        # Check columns
        columns = [[self.board[i] for i in range(len(self.board)) if i % 3 == j] for j in range(3)]
        for column in columns:
            if all(spot == "X" for spot in column) or all(spot == "O" for spot in column):
                return True
        # Check diagonals
        diagonals = [[self.board[0], self.board[4], self.board[8]], [self.board[2], self.board[4] ,self.board[6]]]
        for diagonal in diagonals:
            if all(spot == "X" for spot in diagonal) or all(spot == "O" for spot in diagonal):
                return True

        return False

    def is_valid_move(self, move):
        # Move is valid if input is in range 0-8 and the spot on the board is empty.
        if move in range(9) and self.board[move] == " ":
            return True
        else:
            return False

    def make_move(self, player):
        # Uses the Player class to make a move.
        try:
            move = player.get_move(self)
            if not self.is_valid_move(move):
                raise ValueError
            # If the move is valid, modify the board
            self.board[move] = player.letter  
        except ValueError:
            if isinstance(player, HumanPlayer):
                print("Invalid move. Please try again.")  # Display an error message if the player is a human.
            self.make_move(player) 

    def is_board_full(self):
        if any(spot == " " for spot in self.board):
            return False
        else:
            return True

    def get_available_spots(self):
        return [i for (i, spot) in enumerate(self.board) if spot == " "]

    def play(self, player1, player2):
        # Print the indices of the board
        print("\nBoard indices:")
        self.print_board_indices()
        current_player = player1
        while self.current_winner == None and not self.is_board_full():
            print()
            self.print_board(self.board)
            # If the player is computer, make a brief pause
            if isinstance(current_player, RandomComputerPlayer):
                print("Computer is making a move...")
                time.sleep(0.5)
            self.make_move(current_player)
            # Check if the game is won
            if self.is_won():
                self.current_winner = current_player
            # Change the player
            if current_player == player1:
                current_player = player2
            else:
                current_player = player1
        if self.current_winner != None:
            self.print_board(self.board)
            print(f"{self.current_winner.letter} is the winner!")
        else:
            self.print_board(self.board)
            print("It's a tie!")


if __name__ == "__main__":
    game = TicTacToe()
    human1 = RandomComputerPlayer("X")
    human2 = HumanPlayer("O")
    game.play(human1, human2)
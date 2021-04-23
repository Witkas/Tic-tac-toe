from player import *

class TicTacToe:
    def __init__(self, x_player, o_player):
        self.board = [" " for _ in range(9)]
        self.x_player = x_player
        self.o_player = o_player
        self.current_player = x_player
        self.current_winner = None

    def print_board(self, board):
        grouped_board = [board[i*3:(i+1)*3] for i in range(3)]  # E.g. [1,2,3,4,5,6,7,8,9] --> [[1,2,3],[4,5,6],[7,8,9]]
        for group in grouped_board:
            print("| " + " | ".join(group) + " |")  # Prints each row

    def print_board_indices(self):
        # Prints the arrangement of the indices on the board (used at the beginning of the game).
        indices = [str(i) for i in range(1,10)]
        self.print_board(indices)
    
    def get_winner(self):
        # This function is used to check if all elements in column/row/diagonal match.
        def check_all(list_of_lists):
            for list_ in list_of_lists:
                if all(spot == "X" for spot in list_):
                    return self.x_player
                elif all(spot == "O" for spot in list_):
                    return self.o_player
        
        # Check rows
        rows = [self.board[i*3:(i+1)*3] for i in range(3)]  # E.g. [1,2,3,4,5,6,7,8,9] --> [[1,2,3],[4,5,6],[7,8,9]]
        if check_all(rows) != None:
            return check_all(rows)
        # Check columns
        columns = [[self.board[i] for i in range(len(self.board)) if i % 3 == j] for j in range(3)]
        if check_all(columns) != None:
            return check_all(columns)
        # Check diagonals
        diagonals = [[self.board[0], self.board[4], self.board[8]], [self.board[2], self.board[4] ,self.board[6]]]
        if check_all(diagonals) != None:
            return check_all(diagonals)

        return None

    def is_valid_move(self, move):
        # Move is valid if input is in range 0-8 and chosen spot on the board is empty.
        if move in range(9) and self.board[move] == " ":
            return True
        else:
            return False

    def make_move(self, player):
        # Modifies the board after selecting the spot by a player.
        move = player.get_move(self)
        self.board[move] = player.letter  

    def is_board_full(self):
        if any(spot == " " for spot in self.board):
            return False
        else:
            return True

    def get_available_spots(self):
        return [i for (i, spot) in enumerate(self.board) if spot == " "]

    def play(self, print_game=True):
        # Print the indices of the board
        if print_game:
            print("\nBoard indices:")
            self.print_board_indices()
        # Play until there is a winner or the board is full.
        while self.current_winner == None and not self.is_board_full():
            if print_game:
                print()
            # 1. Current player makes a move
            self.make_move(self.current_player)
            # 2. Check if the game is won
            if self.get_winner() != None:
                self.current_winner = self.current_player
            # 3. Print the board
            if print_game:
                self.print_board(self.board)
            # 4. Change current player
            self.current_player = o_player if self.current_player == x_player else x_player

        print()
        if self.current_winner != None:
            print(f"{self.current_winner.letter} is the winner!")
        else:
            print("It's a tie!")


if __name__ == "__main__":
    x_player = GeniusComputerPlayer("X")
    o_player = HumanPlayer("O")
    game = TicTacToe(x_player, o_player)
    #game.board = [" ", "O", "O", "X", "X", " ", " ", "X", "O"]
    game.play()
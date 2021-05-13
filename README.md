# Tic-tac-toe
This is a tic-tac-toe implemented in Python, featuring different types of computer players, including an advanced AI player that cannot lose.
## How to run
Type the following command in the command line:
##### Windows
    python game.py
##### MacOS/Linux
    python3 game.py
## Types of players
* HumanPlayer - user can decide on which square they want to leave their mark
* RandomComputerPlayer - chooses random spot on the board
* GeniusComputerPlayer - chooses the best possible spot on the board (impossible to win with this one)
* IdiotComputerPlayer - chooses the worst possible spot on the board (this one is funny - pretty hard to lose against it!)
## Changing a player
Simply edit the `x_player` and `o_player` variables at the bottom of `game.py`. <br>
For example, if you want to play together with a friend, you should set `x_player` to `HumanPlayer("X")` and `o_player` to `HumanPlayer("O")`.

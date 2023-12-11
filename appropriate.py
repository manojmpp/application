

# AI module for playing Tic Tac Toe
import random
from typing import List, Tuple

def initialize_board() -> List[str]:
    """
    Initializes the game board with empty spaces.
    """
    return [' '] * 9

def check_winner(board: List[str]) -> str:
    """
    Checks if there is a winner or if the game ends in a tie.
    Returns the winner ('X' or 'O') or 'T' for a tie.
    """
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # columns
        (0, 4, 8), (2, 4, 6)             # diagonals
    ]

    for combination in winning_combinations:
        values = [board[i] for i in combination]
        if values == ['X', 'X', 'X']:
            return 'X'
        elif values == ['O', 'O', 'O']:
            return 'O'

    if ' ' not in board:
        return 'T'

    return ' '

def play_game():
    """
    Plays a game of Tic Tac Toe between two players.
    """
    board = initialize_board()
    current_player = 'X'

    while True:
        print_board(board)
        move = get_move(board, current_player)
        make_move(board, move, current_player)
        winner = check_winner(board)

        if winner != ' ':
            print(f"{winner} wins!")
            break

def get_move(board: List[str], player: str) -> int:
    """
    Gets a valid move from the current player.
    """
    while True:
        move = input(f"{player}'s turn. Enter your move (1-9): ")
        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid move. Please enter a number between 1 and 9.")
            continue

        move_index = int(move) - 1
        if board[move_index] != ' ':
            print("Invalid move. That space is already occupied.")
            continue

        return move_index

def make_move(board: List[str], move: int, player: str):
    """
    Makes a move on the game board.
    """
    board[move] = player

def print_board(board: List[str]):
    """
    Prints the current state of the game board.
    """
    for row in range(0, 9, 3):
        print
from commons.models import Coordinate
from commons.utils import *

WHITE = 0
BLACK = 1
GREEN = 2
RED = 3

# Example: colored_board = color_board(board, [Coordinate(1,1), Coordinate(3,5)])
def color_board(board, possible_destinations):
    colored_board = [
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0]]
    
    for dst in possible_destinations:
        if board[dst.row][dst.column] != '.':
            colored_board[dst.row][dst.column] = RED
        else:
            colored_board[dst.row][dst.column] = GREEN

    return colored_board
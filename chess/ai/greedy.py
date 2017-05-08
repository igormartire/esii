from chess.core.models import Coordinate
from chess.core.moving import move
from chess.core.possible_destinations import destinations
from chess.ai.score import score_board
from chess.core.utils import BLACK_PIECES


def greedy_move(board):
    best_move = None
    best_value = -10000
    for row in range(8):
        for column in range(8):
            piece = board[row][column]
            if piece in BLACK_PIECES:
                src = Coordinate(row, column)
                dests = destinations(board, src)
                for dest in dests:
                    possible_board = move(board, src, dest)
                    possible_value = score_board(possible_board)
                    if possible_value > best_value:
                        best_move = (src, dest)
    return best_move

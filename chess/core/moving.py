from chess.core.models import Piece, Coordinate
import copy


def move(board, src, dest):
    board = copy.deepcopy(board)
    piece = board[src.row][src.column]
    board[src.row][src.column] = Piece.NONE
    board[dest.row][dest.column] = piece
    return board

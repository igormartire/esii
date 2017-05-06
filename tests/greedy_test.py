from chess.ai.greedy import greedy_move
from chess.core.models import Piece, Coordinate
from chess.core.utils import empty_board

def test_greedy_move_chooses_dumb_eating_move():
    board = empty_board()

    board[0][0] = Piece.BLACK_QUEEN
    board[1][1] = Piece.WHITE_PAWN
    board[2][2] = Piece.WHITE_PAWN

    assert greedy_move(board) == (Coordinate(0, 0), Coordinate(1, 1))
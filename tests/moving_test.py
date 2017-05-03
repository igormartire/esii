from chess.core.moving import diagonal_moves
from chess.core.models import Piece, Coordinate
from chess.core.utils import empty_board

def test_diagonal_moves():
    board = empty_board()
    assert diagonal_moves(board, Coordinate(4,4)) == set([
        Coordinate(3,3), Coordinate(2,2), Coordinate(1,1),
        Coordinate(0,0), Coordinate(5,5), Coordinate(6,6),
        Coordinate(7,7), Coordinate(3,5), Coordinate(2,6),
        Coordinate(1,7), Coordinate(5,3), Coordinate(6,2),
        Coordinate(7,1)
    ])

def test_diagonal_moves_with_blocking_piece():
    board = empty_board()
    board[1][1] = Piece.WHITE_PAWN
    assert diagonal_moves(board, Coordinate(4,4)) == set([
        Coordinate(3,3), Coordinate(2,2), Coordinate(1,1),
        Coordinate(5,5), Coordinate(6,6), Coordinate(7,7),
        Coordinate(3,5), Coordinate(2,6), Coordinate(1,7),
        Coordinate(5,3), Coordinate(6,2), Coordinate(7,1)
    ])

def test_diagonal_moves_non_main_diagonal():
    board = empty_board()
    board[1][1] = Piece.WHITE_PAWN
    assert diagonal_moves(board, Coordinate(1,4)) == set([
        Coordinate(0,3), Coordinate(0,5), Coordinate(2,3),
        Coordinate(3,2), Coordinate(4,1), Coordinate(5,0),
        Coordinate(2,5), Coordinate(3,6), Coordinate(4,7)
    ])
from chess.ai.score import score_board
from chess.core.models import Piece
from chess.core.utils import initial_board

def test_score_board_should_return_0():
    assert score_board(initial_board()) == 0

def test_score_board_should_return_5():
    board = initial_board()
    board[7][0] = Piece.NONE
    assert score_board(board) == 5

def test_score_board_should_return_6():
    board = initial_board()
    board[0][2] = Piece.NONE # -3
    board[1][1] = Piece.NONE # -1
    board[6][0] = Piece.NONE # +1
    board[7][3] = Piece.NONE # +9
    assert score_board(board) == 6

def test_score_board_should_return_9000():
    board = initial_board()
    board[1][6] = Piece.NONE # -1
    board[1][1] = Piece.NONE # -1
    board[6][3] = Piece.NONE # +1
    board[7][4] = Piece.NONE # +9001
    assert score_board(board) == 9000

from chess.ai.score import score_board
from chess.core.models import Piece
from chess.core.game import Game


def test_score_board_should_return_0():
    game = Game()
    assert score_board(game.board) == 0


def test_score_board_should_return_5():
    game = Game()
    game.board[7][0] = Piece.NONE
    assert score_board(game.board) == 5


def test_score_board_should_return_6():
    game = Game()
    game.board[0][2] = Piece.NONE  # -3
    game.board[1][1] = Piece.NONE  # -1
    game.board[6][0] = Piece.NONE  # +1
    game.board[7][3] = Piece.NONE  # +9
    assert score_board(game.board) == 6


def test_score_board_should_return_9000():
    game = Game()
    game.board[1][6] = Piece.NONE  # -1
    game.board[1][1] = Piece.NONE  # -1
    game.board[6][3] = Piece.NONE  # +1
    game.board[7][4] = Piece.NONE  # +9001
    assert score_board(game.board) == 9000

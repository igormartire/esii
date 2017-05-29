from chess.ai.greedy import greedy_move
from chess.core.models import Piece, Coordinate
from chess.core.utils import empty_board
from chess.core.game import Game


def test_greedy_move_chooses_dumb_eating_move():
    game = Game()
    game.board = empty_board()

    game.board[0][0] = Piece.BLACK_QUEEN
    game.board[1][1] = Piece.WHITE_PAWN
    game.board[2][2] = Piece.WHITE_PAWN

    assert greedy_move(game) == (Coordinate(0, 0), Coordinate(1, 1))

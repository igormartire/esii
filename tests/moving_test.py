from chess.core.moving import move
from chess.core.models import Coordinate, Piece
from chess.core.game import Game
import mock


@mock.patch('chess.core.moving.castling')
@mock.patch('chess.core.moving.promotion')
@mock.patch('chess.core.moving.en_passant')
def test_move(castling, promotion, en_passant):
    game = Game()

    assert(game.board[7][0] == Piece.WHITE_ROOK)
    assert(game.board[7][4] == Piece.WHITE_KING)

    move(game, Coordinate(7, 0), Coordinate(7, 4))

    assert(game.board[7][0] == Piece.NONE)
    assert(game.board[7][4] == Piece.WHITE_ROOK)

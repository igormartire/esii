from chess.core.moving import move
from chess.core.models import Coordinate, Piece
from chess.core.game import Game
from chess.core.possible_destinations import destinations
from chess.core.utils import _, K, k, Q, q, R, r, N, n, B, b, P, p, piece_at


def test_castling_left_white_rook():
    game = Game()
    game.board = [[_, _, _, _, k, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [R, _, _, _, K, _, _, _]]
    white_king_src = Coordinate(7, 4)
    white_king_dest = white_king_src.left().left()
    white_rook_src = Coordinate(7, 0)

    assert(white_king_dest in destinations(game, white_king_src))

    move(game, white_king_src, white_king_dest)

    assert(piece_at(game.board, white_rook_src) == Piece.NONE)
    assert(piece_at(game.board, white_king_src) == Piece.NONE)
    assert(piece_at(game.board, white_king_dest) == Piece.WHITE_KING)
    assert(piece_at(game.board, white_king_dest.right()) == Piece.WHITE_ROOK)


def test_castling_right_white_rook():
    game = Game()
    game.board = [[_, _, _, _, k, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, K, _, _, R]]
    white_king_src = Coordinate(7, 4)
    white_king_dest = white_king_src.right().right()
    white_rook_src = Coordinate(7, 7)

    assert(white_king_dest in destinations(game, white_king_src))

    move(game, white_king_src, white_king_dest)

    assert(piece_at(game.board, white_rook_src) == Piece.NONE)
    assert(piece_at(game.board, white_king_src) == Piece.NONE)
    assert(piece_at(game.board, white_king_dest) == Piece.WHITE_KING)
    assert(piece_at(game.board, white_king_dest.left()) == Piece.WHITE_ROOK)

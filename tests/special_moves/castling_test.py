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


def test_castling_left_black_rook():
    game = Game()
    game.board = [[r, _, _, _, k, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, K, _, _, _]]
    black_king_src = Coordinate(0, 4)
    black_king_dest = black_king_src.left().left()
    black_rook_src = Coordinate(0, 0)

    assert(black_king_dest in destinations(game, black_king_src))

    move(game, black_king_src, black_king_dest)

    assert(piece_at(game.board, black_rook_src) == Piece.NONE)
    assert(piece_at(game.board, black_king_src) == Piece.NONE)
    assert(piece_at(game.board, black_king_dest) == Piece.BLACK_KING)
    assert(piece_at(game.board, black_king_dest.right()) == Piece.BLACK_ROOK)


def test_castling_right_black_rook():
    game = Game()
    game.board = [[_, _, _, _, k, _, _, r],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, K, _, _, _]]
    black_king_src = Coordinate(0, 4)
    black_king_dest = black_king_src.right().right()
    black_rook_src = Coordinate(0, 7)

    assert(black_king_dest in destinations(game, black_king_src))

    move(game, black_king_src, black_king_dest)

    assert(piece_at(game.board, black_rook_src) == Piece.NONE)
    assert(piece_at(game.board, black_king_src) == Piece.NONE)
    assert(piece_at(game.board, black_king_dest) == Piece.BLACK_KING)
    assert(piece_at(game.board, black_king_dest.left()) == Piece.BLACK_ROOK)


def test_no_castling_allowed_when_path_is_blocked():
    game = Game()
    game.board = [[_, _, _, _, k, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [R, _, B, _, K, _, _, _]]
    white_king_src = Coordinate(7, 4)
    white_king_dest = white_king_src.left().left()
    white_rook_src = Coordinate(7, 0)

    assert(white_king_dest not in destinations(game, white_king_src))


def test_no_castling_allowed_when_in_check():
    game = Game()
    game.board = [[_, _, _, _, k, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, p, _, _, _, _],
                  [R, _, _, _, K, _, _, _]]
    white_king_src = Coordinate(7, 4)
    white_king_dest = white_king_src.left().left()
    white_rook_src = Coordinate(7, 0)

    assert(white_king_dest not in destinations(game, white_king_src))

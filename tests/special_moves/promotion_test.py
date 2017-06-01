from chess.core.moving import move
from chess.core.models import Piece, Coordinate
from chess.core.utils import empty_board, set_at, piece_at
from chess.core.game import Game


def test_promotion_change_to_specified_piece():
    game = Game()
    game.board = empty_board()
    white_pawn_coordinate_src = Coordinate(1, 4)
    white_pawn_coordinate_dest = white_pawn_coordinate_src.up()
    set_at(game.board, white_pawn_coordinate_src, Piece.WHITE_PAWN)

    def promotion_callback():
        return Piece.WHITE_KNIGHT

    move(game,
         white_pawn_coordinate_src,
         white_pawn_coordinate_dest,
         promotion_callback)

    assert (piece_at(game.board, white_pawn_coordinate_dest) ==
            Piece.WHITE_KNIGHT)


def test_promotion_change_to_white_queen():
    game = Game()
    game.board = empty_board()
    white_pawn_coordinate_src = Coordinate(1, 4)
    white_pawn_coordinate_dest = white_pawn_coordinate_src.up()
    set_at(game.board, white_pawn_coordinate_src, Piece.WHITE_PAWN)

    move(game,
         white_pawn_coordinate_src,
         white_pawn_coordinate_dest)

    assert (piece_at(game.board, white_pawn_coordinate_dest) ==
            Piece.WHITE_QUEEN)


def test_promotion_change_to_black_queen():
    game = Game()
    game.board = empty_board()
    black_pawn_coordinate_src = Coordinate(6, 4)
    black_pawn_coordinate_dest = black_pawn_coordinate_src.down()
    set_at(game.board, black_pawn_coordinate_src, Piece.BLACK_PAWN)

    move(game,
         black_pawn_coordinate_src,
         black_pawn_coordinate_dest)

    assert (piece_at(game.board, black_pawn_coordinate_dest) ==
            Piece.BLACK_QUEEN)


def test_no_promotion():
    game = Game()
    game.board = empty_board()
    white_pawn_coordinate_src = Coordinate(2, 4)
    white_pawn_coordinate_dest = white_pawn_coordinate_src.up()
    set_at(game.board, white_pawn_coordinate_src, Piece.WHITE_PAWN)

    def promotion_callback():
        return Piece.WHITE_KNIGHT

    move(game,
         white_pawn_coordinate_src,
         white_pawn_coordinate_dest,
         promotion_callback)

    assert (piece_at(game.board, white_pawn_coordinate_dest) ==
            Piece.WHITE_PAWN)

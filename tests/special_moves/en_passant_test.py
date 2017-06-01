from chess.core.moving import move
from chess.core.possible_destinations import destinations
from chess.core.models import Piece, Coordinate
from chess.core.utils import empty_board, set_at, piece_at
from chess.core.game import Game


def test_en_passant_right_after_double_step():
    game = Game()
    white_pawn_coordinate_src = Coordinate(3, 4)
    white_pawn_coordinate_dest = white_pawn_coordinate_src.up().right()
    black_pawn_coordinate_src = Coordinate(1, 5)
    black_pawn_coordinate_dest = black_pawn_coordinate_src.down(2)
    set_at(game.board, white_pawn_coordinate_src, Piece.WHITE_PAWN)

    assert(white_pawn_coordinate_dest not in
           destinations(game, white_pawn_coordinate_src))

    move(game, black_pawn_coordinate_src, black_pawn_coordinate_dest)

    assert(white_pawn_coordinate_dest in 
           destinations(game, white_pawn_coordinate_src))

    move(game, white_pawn_coordinate_src, white_pawn_coordinate_dest)

    assert(piece_at(game.board, white_pawn_coordinate_dest) ==
           Piece.WHITE_PAWN)

    assert(piece_at(game.board, white_pawn_coordinate_dest.down()) ==
           Piece.NONE)

def test_no_en_passant_if_single_step():
    game = Game()
    white_pawn_coordinate_src = Coordinate(3, 4)
    white_pawn_coordinate_dest = white_pawn_coordinate_src.up().right()
    black_pawn_coordinate_src = Coordinate(2, 5)
    black_pawn_coordinate_dest = black_pawn_coordinate_src.down()
    set_at(game.board, white_pawn_coordinate_src, Piece.WHITE_PAWN)
    set_at(game.board, black_pawn_coordinate_src, Piece.BLACK_PAWN)

    assert(white_pawn_coordinate_dest in
           destinations(game, white_pawn_coordinate_src))

    move(game, black_pawn_coordinate_src, black_pawn_coordinate_dest)

    assert(white_pawn_coordinate_dest not in 
           destinations(game, white_pawn_coordinate_src))

def test_no_en_passant_after_a_turn():
    game = Game()
    white_pawn_coordinate_src = Coordinate(3, 4)
    white_pawn_coordinate_dest = white_pawn_coordinate_src.up().right()
    black_pawn_coordinate_src = Coordinate(1, 5)
    black_pawn_coordinate_dest = black_pawn_coordinate_src.down(2)
    set_at(game.board, white_pawn_coordinate_src, Piece.WHITE_PAWN)

    assert(white_pawn_coordinate_dest not in
           destinations(game, white_pawn_coordinate_src))

    move(game, black_pawn_coordinate_src, black_pawn_coordinate_dest)

    assert(white_pawn_coordinate_dest in 
           destinations(game, white_pawn_coordinate_src))

    move(game, Coordinate(7,1), Coordinate(5, 2)) # white knight move
    move(game, Coordinate(0,1), Coordinate(2, 2)) # black knight move

    assert(white_pawn_coordinate_dest not in
           destinations(game, white_pawn_coordinate_src))
    
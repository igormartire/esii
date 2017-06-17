from chess.core.moving import move
from chess.core.models import Player, Coordinate
from chess.core.game import Game
from chess.core.destinations import (is_check_for_player,
                                              is_checkmate_for_player)
from chess.core.utils import _, K, k, Q, q, R, r, N, n, B, b, P, p


def new_game_with_no_castling():
    game = Game()
    game.state.allow_castling_white_king = False
    game.state.allow_castling_left_white_rook = False
    game.state.allow_castling_right_white_rook = False
    game.state.allow_castling_black_king = False
    game.state.allow_castling_left_black_rook = False
    game.state.allow_castling_right_black_rook = False
    return game


def test_check():
    game = new_game_with_no_castling()
    game.board = [[_, _, _, _, k, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, Q, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, K, _, _, _]]
    white_queen_src = Coordinate(2, 5)
    white_queen_dest = white_queen_src.up()

    assert(not is_check_for_player(game, Player.BLACK))

    move(game, white_queen_src, white_queen_dest)

    assert(is_check_for_player(game, Player.BLACK))


def test_checkmate():
    game = new_game_with_no_castling()
    game.board = [[_, _, _, _, k, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, P, _, Q, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, K, _, _, _]]
    white_queen_src = Coordinate(2, 5)
    white_queen_dest = white_queen_src.up().left()

    assert(not is_checkmate_for_player(game, Player.BLACK))

    move(game, white_queen_src, white_queen_dest)

    assert(is_checkmate_for_player(game, Player.BLACK))

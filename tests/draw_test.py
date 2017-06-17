from chess.core.moving import move
from chess.core.models import Player, Coordinate
from chess.core.game import Game
from chess.core.possible_destinations import (is_stalemate_for_player,
                                              is_impossible_checkmate)
from chess.core.utils import _, K, k, Q, q, R, r, N, n, B, b, P, p, print_board


def new_game_with_no_castling():
    game = Game()
    game.state.allow_castling_white_king = False
    game.state.allow_castling_left_white_rook = False
    game.state.allow_castling_right_white_rook = False
    game.state.allow_castling_black_king = False
    game.state.allow_castling_left_black_rook = False
    game.state.allow_castling_right_black_rook = False
    return game


def test_draw_by_stalemate():
    game = new_game_with_no_castling()
    game.board = [[_, _, _, _, k, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, R, _, R, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, K, _, _, Q]]
    white_queen_src = Coordinate(7, 7)
    white_queen_dest = Coordinate(1, 7)

    assert(not is_stalemate_for_player(game, Player.BLACK))

    move(game, white_queen_src, white_queen_dest)

    assert(is_stalemate_for_player(game, Player.BLACK))

def test_draw_by_impossible_checkmate_king_vs_king():
    game = new_game_with_no_castling()
    game.board = [[_, _, _, _, k, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, q, _, _, _, _, _, _],
                  [K, _, _, _, _, _, _, _]]
    white_king_src = Coordinate(7, 0)
    white_king_dest = Coordinate(6, 1)

    assert(not is_impossible_checkmate(game))

    move(game, white_king_src, white_king_dest)

    assert(is_impossible_checkmate(game))

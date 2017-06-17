from chess.core.moving import move
from chess.core.models import Player, Coordinate
from chess.core.game import Game
from chess.core.query import is_stalemate_for_player, is_impossible_checkmate
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


def test_draw_by_impossible_checkmate_king_vs_king_bishop():
    game = new_game_with_no_castling()
    game.board = [[_, _, _, _, k, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, b, _, _, _, _, _, _],
                  [_, b, _, _, _, _, _, _],
                  [K, _, _, _, _, _, _, _]]
    white_king_src = Coordinate(7, 0)
    white_king_dest = Coordinate(6, 1)

    assert(not is_impossible_checkmate(game))

    move(game, white_king_src, white_king_dest)

    assert(is_impossible_checkmate(game))


def test_draw_by_impossible_checkmate_king_vs_king_knight():
    game = new_game_with_no_castling()
    game.board = [[_, _, _, _, k, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, b, _, _, _, _, _, _],
                  [_, n, _, _, _, _, _, _],
                  [K, _, _, _, _, _, _, _]]
    white_king_src = Coordinate(7, 0)
    white_king_dest = Coordinate(6, 1)

    assert(not is_impossible_checkmate(game))

    move(game, white_king_src, white_king_dest)

    assert(is_impossible_checkmate(game))


def test_draw_by_impossible_checkmate_king_bishop_vs_king_bishop():
    # bishops on the same color
    game = new_game_with_no_castling()
    game.board = [[_, _, _, _, k, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, b, _, _, _, _, _, _],
                  [_, b, _, _, _, _, _, _],
                  [K, _, _, _, _, B, _, _]]
    white_king_src = Coordinate(7, 0)
    white_king_dest = Coordinate(6, 1)

    assert(not is_impossible_checkmate(game))

    move(game, white_king_src, white_king_dest)

    assert(is_impossible_checkmate(game))


def test_not_draw_by_impossible_checkmate_king_bishop_vs_king_bishop():
    # bishops on different colors
    game = new_game_with_no_castling()
    game.board = [[_, _, _, _, k, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, b, _, _, _, _, _, _],
                  [_, b, _, _, _, _, _, _],
                  [K, _, _, _, B, _, _, _]]
    white_king_src = Coordinate(7, 0)
    white_king_dest = Coordinate(6, 1)

    assert(not is_impossible_checkmate(game))

    move(game, white_king_src, white_king_dest)

    assert(not is_impossible_checkmate(game))


# def test_threefold_repetition():
#     draw_allowed = False
#     game = new_game_with_no_castling()
#     game.register_draw_allowed_callback = lambda: draw_allowed = True
#     game.board = [
#         [_, _, _, _, _, _, _, k],
#         [Q, _, _, _, _, _, _, _],
#         [_, _, _, _, N, _, _, _],
#         [_, _, _, _, _, _, _, _],
#         [_, _, _, _, _, _, _, _],
#         [_, _, _, _, p, _, _, _],
#         [_, _, _, _, _, _, _, _],
#         [_, _, _, _, K, _, R, _]]
#     white_rook_src = Coordinate(7, 6)
#     white_rook_dest = white_rook_src.right()
#     black_king_src = Coordinate(0, 7)
#     black_king_dest = black_king_src.left()

#     move(game, Coordinate(5, 4), Coordinate(6, 4))
#     # posicao A; count = 1
#     assert(not draw_allowed)

#     move(game, white_rook_src, white_rook_dest)
#     move(game, black_king_src, black_king_dest)
#     # posicao B; count = 1
#     assert(not draw_allowed)

#     move(game, white_rook_dest, white_rook_src)
#     move(game, black_king_dest, black_king_src)
#     # posicao A; count = 2
#     assert(not draw_allowed)

#     move(game, white_rook_src, white_rook_dest)
#     move(game, black_king_src, black_king_dest)
#     # posicao B; count = 2
#     assert(not draw_allowed)

#     move(game, white_rook_dest, white_rook_src)
#     move(game, black_king_dest, black_king_src)
#     # posicao A; count = 3
#     assert(draw_allowed)
#     draw_allowed = False

#     move(game, white_rook_src, white_rook_dest)
#     move(game, black_king_src, black_king_dest)
#     # posicao B; count = 3
#     assert(draw_allowed)
#     draw_allowed = False

#     move(game, white_rook_dest, white_rook_src)
#     move(game, black_king_dest, black_king_src)
#     # posicao A; count = 4
#     assert(draw_allowed)

from chess.core.moving import move
from chess.core.models import Player, Coordinate, Piece
from chess.core.game import Game
from chess.core.query import (is_check_for_player,
                              is_checkmate_for_player,
                              is_attacked)
from chess.core.utils import _, K, k, Q, q, R, r, N, n, B, b, P, p
import mock


##############
# UNIT TESTS #
##############


@mock.patch('chess.core.query.piece_at')
@mock.patch('chess.core.query.destinations')
def test_is_attacked(destinations, piece_at):
    game_stub = Game()
    game_stub.board = ['A', 'B', 'C', 'non-sense', 'i-am-mocked']
    pos_stub = Coordinate(123, -321)
    attacked_player = Player.WHITE

    def piece_at_mock(board, coord):
        assert(board == game_stub.board)
        if coord == Coordinate(0, 1):
            return Piece.WHITE_BISHOP
        if coord == Coordinate(0, 2):
            return Piece.BLACK_QUEEN
        else:
            return Piece.NONE

    piece_at.side_effect = piece_at_mock
    destinations.return_value = [pos_stub]

    assert(is_attacked(game_stub, pos_stub, attacked_player))

    assert(piece_at.call_count == 3)  # for coordinates (0,0), (0,1), (0,2)
    assert(destinations.call_count == 1)  # for attacker piece BLACK_QUEEN


@mock.patch('chess.core.query.destinations')
@mock.patch('chess.core.query.piece_at')
def test_is_not_attacked(piece_at, destinations):
    game_stub = Game()
    game_stub.board = ['A', 'B', 'C', 'non-sense', 'i-am-mocked']
    pos_stub = Coordinate(123, -321)
    attacked_player = Player.BLACK

    def piece_at_mock(board, coord):
        assert(board == game_stub.board)
        if coord == Coordinate(0, 1):
            return Piece.WHITE_BISHOP
        if coord == Coordinate(0, 2):
            return Piece.WHITE_QUEEN
        else:
            return Piece.NONE

    piece_at.side_effect = piece_at_mock
    destinations.return_value = [Coordinate(0, 0)]  # not pos_stub

    assert(not is_attacked(game_stub, pos_stub, attacked_player))

    assert(piece_at.call_count == 64)  # for coordinates (0,0), (0,1), (0,2)
    # for attacker pieces BISHOP and QUEEN
    assert(destinations.call_count == 2)


@mock.patch('chess.core.query.is_attacked')
@mock.patch('chess.core.query.get_piece_coordinate')
def test_is_check_for_player_white(get_piece_coordinate, is_attacked):
    game_stub = Game()
    game_stub.board = ['A', 'B', 'C', 'non-sense', 'i-am-mocked']
    king_pos_stub = Coordinate(123, 456)
    checked_player = Player.WHITE

    get_piece_coordinate.return_value = king_pos_stub
    is_attacked.return_value = True

    assert(is_check_for_player(game_stub, checked_player))

    args, kwargs = get_piece_coordinate.call_args
    assert args == (game_stub.board, Piece.WHITE_KING)
    assert kwargs == {}

    args, kwargs = is_attacked.call_args
    assert args == (game_stub, king_pos_stub, checked_player)
    assert kwargs == {}


@mock.patch('chess.core.query.is_attacked')
@mock.patch('chess.core.query.get_piece_coordinate')
def test_is_not_check_for_player_white(get_piece_coordinate, is_attacked):
    game_stub = Game()
    game_stub.board = ['A', 'B', 'C', 'non-sense', 'i-am-mocked']
    king_pos_stub = Coordinate(123, 456)
    checked_player = Player.WHITE

    get_piece_coordinate.return_value = king_pos_stub
    is_attacked.return_value = False

    assert(not is_check_for_player(game_stub, checked_player))

    args, kwargs = get_piece_coordinate.call_args
    assert args == (game_stub.board, Piece.WHITE_KING)
    assert kwargs == {}

    args, kwargs = is_attacked.call_args
    assert args == (game_stub, king_pos_stub, checked_player)
    assert kwargs == {}


@mock.patch('chess.core.query.is_attacked')
@mock.patch('chess.core.query.get_piece_coordinate')
def test_is_check_for_player_black(get_piece_coordinate, is_attacked):
    game_stub = Game()
    game_stub.board = ['A', 'B', 'C', 'non-sense', 'i-am-mocked']
    king_pos_stub = Coordinate(123, 456)
    checked_player = Player.BLACK

    get_piece_coordinate.return_value = king_pos_stub
    is_attacked.return_value = True

    assert(is_check_for_player(game_stub, checked_player))

    args, kwargs = get_piece_coordinate.call_args
    assert args == (game_stub.board, Piece.BLACK_KING)
    assert kwargs == {}

    args, kwargs = is_attacked.call_args
    assert args == (game_stub, king_pos_stub, checked_player)
    assert kwargs == {}


@mock.patch('chess.core.query.is_attacked')
@mock.patch('chess.core.query.get_piece_coordinate')
def test_is_not_check_for_player_black(get_piece_coordinate, is_attacked):
    game_stub = Game()
    game_stub.board = ['A', 'B', 'C', 'non-sense', 'i-am-mocked']
    king_pos_stub = Coordinate(123, 456)
    checked_player = Player.BLACK

    get_piece_coordinate.return_value = king_pos_stub
    is_attacked.return_value = False

    assert(not is_check_for_player(game_stub, checked_player))

    args, kwargs = get_piece_coordinate.call_args
    assert args == (game_stub.board, Piece.BLACK_KING)
    assert kwargs == {}

    args, kwargs = is_attacked.call_args
    assert args == (game_stub, king_pos_stub, checked_player)
    assert kwargs == {}


#####################
# INTEGRATION TESTS #
#####################


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

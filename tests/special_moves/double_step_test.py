from chess.core.destinations import destinations
from chess.core.models import Piece, Coordinate
from chess.core.utils import empty_board, set_at
from chess.core.game import Game


def test_white_pawn_can_double_step():
    game = Game()
    game.board = empty_board()
    for c in range(8):
        pawn_coordinate = Coordinate(6, c)
        set_at(game.board, pawn_coordinate, Piece.WHITE_PAWN)

        actual_destinations = destinations(game, pawn_coordinate)

        assert Coordinate(4, c) in actual_destinations


def test_black_pawn_can_double_step():
    game = Game()
    game.board = empty_board()
    for c in range(8):
        pawn_coordinate = Coordinate(1, c)
        set_at(game.board, pawn_coordinate, Piece.BLACK_PAWN)

        actual_destinations = destinations(game, pawn_coordinate)

        assert Coordinate(3, c) in actual_destinations


def test_white_pawn_can_double_step_and_still_eat_diagonally():
    game = Game()
    game.board = empty_board()
    pawn_coordinate = Coordinate(6, 3)
    set_at(game.board, pawn_coordinate, Piece.WHITE_PAWN)
    set_at(game.board, pawn_coordinate.up().left(), Piece.BLACK_QUEEN)

    actual_destinations = destinations(game, pawn_coordinate)

    assert Coordinate(5, 2) in actual_destinations
    assert Coordinate(4, 3) in actual_destinations


def test_black_pawn_can_double_step_and_still_eat_diagonally():
    game = Game()
    game.board = empty_board()
    pawn_coordinate = Coordinate(1, 5)
    set_at(game.board, pawn_coordinate, Piece.BLACK_PAWN)
    set_at(game.board, pawn_coordinate.down().left(), Piece.WHITE_ROOK)

    actual_destinations = destinations(game, pawn_coordinate)

    assert Coordinate(2, 4) in actual_destinations
    assert Coordinate(3, 5) in actual_destinations


def test_white_pawn_cannot_eat_with_double_step():
    game = Game()
    game.board = empty_board()
    pawn_coordinate = Coordinate(6, 3)
    set_at(game.board, pawn_coordinate, Piece.WHITE_PAWN)
    set_at(game.board, pawn_coordinate.up(2), Piece.BLACK_QUEEN)

    actual_destinations = destinations(game, pawn_coordinate)

    assert Coordinate(4, 3) not in actual_destinations


def test_black_pawn_cannot_eat_with_double_step():
    game = Game()
    game.board = empty_board()
    pawn_coordinate = Coordinate(1, 5)
    set_at(game.board, pawn_coordinate, Piece.BLACK_PAWN)
    set_at(game.board, pawn_coordinate.down(2), Piece.WHITE_ROOK)

    actual_destinations = destinations(game, pawn_coordinate)

    assert Coordinate(3, 5) not in actual_destinations


def test_white_pawn_cannot_double_step():
    game = Game()
    game.board = empty_board()
    pawn_coordinate = Coordinate(5, 0)
    set_at(game.board, pawn_coordinate, Piece.WHITE_PAWN)

    actual_destinations = destinations(game, pawn_coordinate)

    assert Coordinate(3, 0) not in actual_destinations


def test_black_pawn_cannot_double_step():
    game = Game()
    game.board = empty_board()
    pawn_coordinate = Coordinate(2, 0)
    set_at(game.board, pawn_coordinate, Piece.BLACK_PAWN)

    actual_destinations = destinations(game, pawn_coordinate)

    assert Coordinate(4, 0) not in actual_destinations


def test_white_pawn_cannot_double_step_when_path_is_blocked():
    game = Game()
    game.board = empty_board()
    pawn_coordinate = Coordinate(6, 0)
    set_at(game.board, pawn_coordinate, Piece.WHITE_PAWN)

    actual_destinations = destinations(game, pawn_coordinate)
    assert Coordinate(4, 0) in actual_destinations

    set_at(game.board, pawn_coordinate.up(), Piece.BLACK_PAWN)

    actual_destinations = destinations(game, pawn_coordinate)
    assert Coordinate(4, 0) not in actual_destinations


def test_black_pawn_cannot_double_step_when_path_is_blocked():
    game = Game()
    game.board = empty_board()
    pawn_coordinate = Coordinate(1, 0)
    set_at(game.board, pawn_coordinate, Piece.BLACK_PAWN)

    actual_destinations = destinations(game, pawn_coordinate)
    assert Coordinate(3, 0) in actual_destinations

    set_at(game.board, pawn_coordinate.down(), Piece.WHITE_PAWN)

    actual_destinations = destinations(game, pawn_coordinate)
    assert Coordinate(3, 0) not in actual_destinations

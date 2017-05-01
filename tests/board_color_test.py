from chess.core.coloring import color_board
from chess.core.models import Color, Coordinate
from chess.core.utils import INITIAL_BOARD


def test_board_color_should_color_black_and_white():
    W = Color.WHITE
    B = Color.BLACK

    actual = color_board(INITIAL_BOARD, [])
    expected = [[W, B, W, B, W, B, W, B],
                [B, W, B, W, B, W, B, W],
                [W, B, W, B, W, B, W, B],
                [B, W, B, W, B, W, B, W],
                [W, B, W, B, W, B, W, B],
                [B, W, B, W, B, W, B, W],
                [W, B, W, B, W, B, W, B],
                [B, W, B, W, B, W, B, W]]

    assert actual == expected


def test_board_color_should_color_red_and_green():
    W = Color.WHITE
    B = Color.BLACK
    G = Color.GREEN
    R = Color.RED

    actual = color_board(INITIAL_BOARD, [Coordinate(1, 1), Coordinate(2, 1)])
    expected = [[W, B, W, B, W, B, W, B],
                [B, R, B, W, B, W, B, W],
                [W, G, W, B, W, B, W, B],
                [B, W, B, W, B, W, B, W],
                [W, B, W, B, W, B, W, B],
                [B, W, B, W, B, W, B, W],
                [W, B, W, B, W, B, W, B],
                [B, W, B, W, B, W, B, W]]

    assert actual == expected

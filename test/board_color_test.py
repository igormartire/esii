import sys
sys.path.append('src')
from board_color import *

def test_board_color_should_color_black_and_white():
        actual = color_board(INITIAL_BOARD, [])
        expected = [
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0]]

        assert actual == expected

def test_board_color_should_color_red_and_green():
        actual = color_board(INITIAL_BOARD, [Coordinate(1,1), Coordinate(2,1)])
        expected = [
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 3, 1, 0, 1, 0, 1, 0],
                [0, 2, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0]]

        assert actual == expected
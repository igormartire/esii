from chess.core.models import Piece

o = Piece.NONE
P = Piece.WHITE_PAWN
B = Piece.WHITE_BISHOP
N = Piece.WHITE_KNIGHT
R = Piece.WHITE_ROOK
Q = Piece.WHITE_QUEEN
K = Piece.WHITE_KING
p = Piece.BLACK_PAWN
b = Piece.BLACK_BISHOP
n = Piece.BLACK_KNIGHT
r = Piece.BLACK_ROOK
q = Piece.BLACK_QUEEN
k = Piece.BLACK_KING


def initial_board():
    return [[r, n, b, q, k, b, n, r],
            [p, p, p, p, p, p, p, p],
            [o, o, o, o, o, o, o, o],
            [o, o, o, o, o, o, o, o],
            [o, o, o, o, o, o, o, o],
            [o, o, o, o, o, o, o, o],
            [P, P, P, P, P, P, P, P],
            [R, N, B, Q, K, B, N, R]]


def empty_board():
    return [[o, o, o, o, o, o, o, o],
            [o, o, o, o, o, o, o, o],
            [o, o, o, o, o, o, o, o],
            [o, o, o, o, o, o, o, o],
            [o, o, o, o, o, o, o, o],
            [o, o, o, o, o, o, o, o],
            [o, o, o, o, o, o, o, o],
            [o, o, o, o, o, o, o, o]]


TEST_COLORED_BOARD = [
    [1, 2, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 3, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1]]

BLACK_PIECES = [Piece.BLACK_PAWN,
                Piece.BLACK_BISHOP,
                Piece.BLACK_KNIGHT,
                Piece.BLACK_ROOK,
                Piece.BLACK_QUEEN,
                Piece.BLACK_KING]

WHITE_PIECES = [Piece.WHITE_PAWN,
                Piece.WHITE_BISHOP,
                Piece.WHITE_KNIGHT,
                Piece.WHITE_ROOK,
                Piece.WHITE_QUEEN,
                Piece.WHITE_KING]


def print_board(board):
    for row in board:
        print(row)

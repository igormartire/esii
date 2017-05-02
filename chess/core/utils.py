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

INITIAL_BOARD = [[r, n, b, q, k, b, n, r],  # 8
                 [p, p, p, p, p, p, p, p],  # 7
                 [o, o, o, o, o, o, o, o],  # 6
                 [o, o, o, o, o, o, o, o],  # 5
                 [o, o, o, o, o, o, o, o],  # 4
                 [o, o, o, o, o, o, o, o],  # 3
                 [P, P, P, P, P, P, P, P],  # 2
                 [R, N, B, Q, K, B, N, R]]  # 1
#                 a  b  c  d  e  f  g  h


TEST_COLORED_BOARD = [
    [1, 2, 1, 0, 1, 0, 1, 0],  # 8
    [0, 1, 0, 1, 0, 1, 0, 1],  # 7
    [1, 3, 1, 0, 1, 0, 1, 0],  # 6
    [0, 1, 0, 1, 0, 1, 0, 1],  # 5
    [1, 0, 1, 0, 1, 0, 1, 0],  # 4
    [0, 1, 0, 1, 0, 1, 0, 1],  # 3
    [1, 0, 1, 0, 1, 0, 1, 0],  # 2
    [0, 1, 0, 1, 0, 1, 0, 1]]  # 1
#    a  b  c  d  e  f  g  h


def print_board(board):
    for row in board:
        print(row)

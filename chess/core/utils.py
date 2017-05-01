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

INITIAL_BOARD = [[r, n, b, q, k, b, n, r],
                 [p, p, p, p, p, p, p, p],
                 [o, o, o, o, o, o, o, o],
                 [o, o, o, o, o, o, o, o],
                 [o, o, o, o, o, o, o, o],
                 [o, o, o, o, o, o, o, o],
                 [P, P, P, P, P, P, P, P],
                 [R, N, B, Q, K, B, N, R]]


def print_board(board):
    for row in board:
        print(row)

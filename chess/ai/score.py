from chess.core.models import Piece

PIECES_SCORE = {
    Piece.NONE: 0,
    Piece.WHITE_PAWN: -1,
    Piece.WHITE_BISHOP: -3,
    Piece.WHITE_KNIGHT: -3,
    Piece.WHITE_ROOK: -5,
    Piece.WHITE_QUEEN: -9,
    Piece.WHITE_KING: -9001,
    Piece.BLACK_PAWN: 1,
    Piece.BLACK_BISHOP: 3 ,
    Piece.BLACK_KNIGHT: 3,
    Piece.BLACK_ROOK: 5,
    Piece.BLACK_QUEEN: 9,
    Piece.BLACK_KING: 9001
}


def score_board(board):
    cpu_score = 0
    for row in range(8):
        for column in range(8):
            piece = board[row][column]
            cpu_score += PIECES_SCORE[piece]
    return cpu_score

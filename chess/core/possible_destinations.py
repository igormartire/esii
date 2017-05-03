from .models import Coordinate, Piece
from .utils import BLACK_PIECES, WHITE_PIECES, INITIAL_BOARD


def is_valid(piece, dest_coord, chess_board):
    print(dest_coord)
    if not dest_coord.inside_board:
        return False

    if dest_coord.row >= 0 and dest_coord.row < 8 and dest_coord.column >= 0 and dest_coord.column < 8:
        dest_piece = chess_board[dest_coord.row][dest_coord.column]
        if dest_piece != Piece.NONE:
            if piece in WHITE_PIECES and dest_piece in WHITE_PIECES:
                return False
            if piece in BLACK_PIECES and dest_piece in BLACK_PIECES:
                return False
        return True
    return False


def destinations(origin_coord, chess_board):
    piece = chess_board[origin_coord.row][origin_coord.column]
    allowed_destinations = []

    if piece == Piece.WHITE_PAWN:
        allowed_destinations = [
            Coordinate(origin_coord.row - 1, origin_coord.column)
        ]

    if piece == Piece.BLACK_PAWN:
        allowed_destinations = [
            Coordinate(origin_coord.row + 1, origin_coord.column)
        ]

    if piece == Piece.WHITE_KNIGHT or piece == Piece.BLACK_KNIGHT:
        allowed_destinations = [
            # Up
            Coordinate(origin_coord.row - 2, origin_coord.column - 1),
            Coordinate(origin_coord.row - 2, origin_coord.column + 1),
            Coordinate(origin_coord.row - 1, origin_coord.column - 2),
            Coordinate(origin_coord.row - 1, origin_coord.column + 2),
            # Down
            Coordinate(origin_coord.row + 2, origin_coord.column - 1),
            Coordinate(origin_coord.row + 2, origin_coord.column + 1),
            Coordinate(origin_coord.row + 1, origin_coord.column - 2),
            Coordinate(origin_coord.row + 1, origin_coord.column + 2),
        ]

    if piece == Piece.WHITE_KING or piece == Piece.BLACK_KING:
        allowed_destinations = [
            Coordinate(origin_coord.row - 1, origin_coord.column - 1),
            Coordinate(origin_coord.row - 1, origin_coord.column - 0),
            Coordinate(origin_coord.row - 1, origin_coord.column + 1),
            Coordinate(origin_coord.row - 0, origin_coord.column - 1),
            Coordinate(origin_coord.row - 0, origin_coord.column + 1),
            Coordinate(origin_coord.row + 1, origin_coord.column - 1),
            Coordinate(origin_coord.row + 1, origin_coord.column - 0),
            Coordinate(origin_coord.row + 1, origin_coord.column + 1),
        ]

    if piece == Piece.WHITE_ROOK or piece == Piece.BLACK_ROOK:
        horizontal_destinations = [Coordinate(origin_coord.row, column)
                                   for column in range(8)]
        vertical_destiantions = [Coordinate(row, origin_coord.column)
                                 for row in range(8)]
        allowed_destinations = horizontal_destinations + vertical_destiantions

    if piece == Piece.WHITE_BISHOP or piece == Piece.BLACK_BISHOP:
        for i in range(8):
            allowed_destinations += [
                Coordinate(origin_coord.row + i, origin_coord.column + i),
                Coordinate(origin_coord.row - i, origin_coord.column + i),
                Coordinate(origin_coord.row - i, origin_coord.column - i),
                Coordinate(origin_coord.row + i, origin_coord.column - i),
            ]

    valid_destinations = [
        coord for coord in allowed_destinations
        if is_valid(piece, coord, chess_board)]

    return valid_destinations

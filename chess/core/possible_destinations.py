from chess.core.models import Coordinate
from chess.core.models import Piece
from chess.core.utils import BLACK_PIECES, WHITE_PIECES


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

    for coordinate in allowed_destinations:
        # Remove coordinates outside board
        invalid_coordinate = False
        if not coordinate.inside_board(chess_board):
            invalid_coordinate = True

        if not invalid_coordinate:
            dest_piece = chess_board[coordinate.row][coordinate.column]
            if dest_piece != Piece.NONE:
                if piece in WHITE_PIECES and dest_piece in WHITE_PIECES:
                    invalid_coordinate = True
                if piece in BLACK_PIECES and dest_piece in BLACK_PIECES:
                    invalid_coordinate = True

        if invalid_coordinate:
            allowed_destinations.remove(coordinate)

    return allowed_destinations

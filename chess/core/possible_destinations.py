from chess.core.models import Coordinate, Piece, Player
from chess.core.utils import (BLACK_PIECES, WHITE_PIECES,
                              initial_board, piece_at, empty_at)
from chess.core.moving import diagonal_moves
from chess.core.check import check


def is_valid(piece, dest, board):
    if not dest.inside_board:
        return False

    if (dest.row >= 0 and dest.row < 8 and
            dest.column >= 0 and dest.column < 8):
        dest_piece = board[dest.row][dest.column]
        if dest_piece != Piece.NONE:
            if piece in WHITE_PIECES and dest_piece in WHITE_PIECES:
                return False
            if piece in BLACK_PIECES and dest_piece in BLACK_PIECES:
                return False
        return True
    return False


def destinations(game, src):
    board = game.board
    piece = board[src.row][src.column]
    allowed_destinations = []

    if piece == Piece.WHITE_PAWN:
        up_middle = Coordinate(src.row - 1, src.column - 0)
        up_left = Coordinate(src.row - 1, src.column - 1)
        up_right = Coordinate(src.row - 1, src.column + 1)
        if is_valid(piece, up_middle, board):
            if board[up_middle.row][up_middle.column] == Piece.NONE:
                allowed_destinations = [
                    Coordinate(src.row - 1, src.column)
                ]
        if is_valid(piece, up_left, board):
            if board[up_left.row][up_left.column] != Piece.NONE:
                allowed_destinations.append(up_left)

        if is_valid(piece, up_right, board):
            if board[up_right.row][up_right.column] != Piece.NONE:
                allowed_destinations.append(up_right)

        if (src.row == 6):  # double step condition
            double_step_coord = src.up(2)
            if (piece_at(board, double_step_coord) == Piece.NONE and
                    piece_at(board, src.up()) == Piece.NONE):
                allowed_destinations.append(double_step_coord)

    if piece == Piece.BLACK_PAWN:
        down_middle = Coordinate(src.row + 1, src.column - 0)
        down_left = Coordinate(src.row + 1, src.column - 1)
        down_right = Coordinate(src.row + 1, src.column + 1)
        if is_valid(piece, down_middle, board):
            if board[down_middle.row][down_middle.column] == Piece.NONE:
                allowed_destinations = [
                    Coordinate(src.row + 1, src.column)
                ]
        if is_valid(piece, down_left, board):
            if board[down_left.row][down_left.column] != Piece.NONE:
                allowed_destinations.append(down_left)
        if is_valid(piece, down_right, board):
            if board[down_right.row][down_right.column] != Piece.NONE:
                allowed_destinations.append(down_right)

        if (src.row == 1):  # double step condition
            double_step_coord = src.down(2)
            if (piece_at(board, double_step_coord) == Piece.NONE and
                    piece_at(board, src.down()) == Piece.NONE):
                allowed_destinations.append(double_step_coord)

    if piece == Piece.WHITE_KNIGHT or piece == Piece.BLACK_KNIGHT:
        allowed_destinations = [
            # Up
            Coordinate(src.row - 2, src.column - 1),
            Coordinate(src.row - 2, src.column + 1),
            Coordinate(src.row - 1, src.column - 2),
            Coordinate(src.row - 1, src.column + 2),
            # Down
            Coordinate(src.row + 2, src.column - 1),
            Coordinate(src.row + 2, src.column + 1),
            Coordinate(src.row + 1, src.column - 2),
            Coordinate(src.row + 1, src.column + 2),
        ]

    if piece == Piece.WHITE_KING or piece == Piece.BLACK_KING:
        allowed_destinations = [
            Coordinate(src.row - 1, src.column - 1),
            Coordinate(src.row - 1, src.column - 0),
            Coordinate(src.row - 1, src.column + 1),
            Coordinate(src.row - 0, src.column - 1),
            Coordinate(src.row - 0, src.column + 1),
            Coordinate(src.row + 1, src.column - 1),
            Coordinate(src.row + 1, src.column - 0),
            Coordinate(src.row + 1, src.column + 1),
        ]

        if (piece == Piece.WHITE_KING and
                game.state.allow_castling_white_king):
            if (game.state.allow_castling_left_white_rook and
                not check(src, Player.WHITE) and
                not check(src.left(1), Player.WHITE) and
                not check(src.left(2), Player.WHITE) and
                empty_at(game.board, src.left(1)) and
                empty_at(game.board, src.left(2)) and
                    empty_at(game.board, src.left(3))):
                allowed_destinations.append(src.left(2))
            if (game.state.allow_castling_right_white_rook and
                not check(src, Player.WHITE) and
                not check(src.right(1), Player.WHITE) and
                not check(src.right(2), Player.WHITE) and
                empty_at(game.board, src.right(1)) and
                    empty_at(game.board, src.right(2))):
                allowed_destinations.append(src.right(2))
        elif (piece == Piece.BLACK_KING and
              game.state.allow_castling_black_king):
            if (game.state.allow_castling_left_black_rook and
                not check(src, Player.BLACK) and
                not check(src.left(1), Player.BLACK) and
                not check(src.left(2), Player.BLACK) and
                empty_at(game.board, src.left(1)) and
                empty_at(game.board, src.left(2)) and
                    empty_at(game.board, src.left(3))):
                allowed_destinations.append(src.left(2))
            if (game.state.allow_castling_right_black_rook and
                not check(src, Player.BLACK) and
                not check(src.right(1), Player.BLACK) and
                not check(src.right(2), Player.BLACK) and
                empty_at(game.board, src.right(1)) and
                    empty_at(game.board, src.right(2))):
                allowed_destinations.append(src.right(2))

    if piece == Piece.WHITE_ROOK or piece == Piece.BLACK_ROOK:
        for left in range(src.column - 1, -1, -1):
            allowed_destinations += [
                Coordinate(src.row, left)
            ]
            if board[src.row][left] != Piece.NONE:
                break
        for right in range(src.column + 1, 8, 1):
            allowed_destinations += [
                Coordinate(src.row, right)
            ]
            if board[src.row][right] != Piece.NONE:
                break
        for down in range(src.row + 1, 8, 1):
            allowed_destinations += [
                Coordinate(down, src.column)
            ]
            if board[down][src.column] != Piece.NONE:
                break
        for up in range(src.row - 1, -1, -1):
            allowed_destinations += [
                Coordinate(up, src.column)
            ]
            if board[up][src.column] != Piece.NONE:
                break

    if piece == Piece.WHITE_BISHOP or piece == Piece.BLACK_BISHOP:
        allowed_destinations = diagonal_moves(board, src)

    if piece == Piece.WHITE_QUEEN or piece == Piece.BLACK_QUEEN:
        for left in range(src.column - 1, -1, -1):
            allowed_destinations += [
                Coordinate(src.row, left)
            ]
            if board[src.row][left] != Piece.NONE:
                break
        for right in range(src.column + 1, 8, 1):
            allowed_destinations += [
                Coordinate(src.row, right)
            ]
            if board[src.row][right] != Piece.NONE:
                break
        for down in range(src.row + 1, 8, 1):
            allowed_destinations += [
                Coordinate(down, src.column)
            ]
            if board[down][src.column] != Piece.NONE:
                break
        for up in range(src.row - 1, -1, -1):
            allowed_destinations += [
                Coordinate(up, src.column)
            ]
            if board[up][src.column] != Piece.NONE:
                break
        allowed_destinations += diagonal_moves(board, src)

    valid_destinations = [
        coord for coord in allowed_destinations
        if is_valid(piece, coord, board)]

    return valid_destinations

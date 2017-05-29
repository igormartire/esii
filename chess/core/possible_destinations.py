from chess.core.models import Coordinate, Piece, Player
from chess.core.utils import (BLACK_PIECES, WHITE_PIECES,
                              initial_board, piece_at, empty_at)
from chess.core.moving import diagonal_moves, move
import copy


def is_valid(game, src, dest):
    if not dest.inside_board():
        return False

    piece = piece_at(game.board, src)

    player = (Player.WHITE
              if piece in WHITE_PIECES
              else Player.BLACK)

    possible_game = copy.deepcopy(game)
    move(possible_game, src, dest)
    if is_check_for_player(possible_game, player):
        return False

    dest_piece = piece_at(game.board, dest)
    if dest_piece != Piece.NONE:
        if piece in WHITE_PIECES and dest_piece in WHITE_PIECES:
            return False
        if piece in BLACK_PIECES and dest_piece in BLACK_PIECES:
            return False

    return True


def is_check_for_player(game, checked_player):
    king = (Piece.WHITE_KING
            if checked_player == Player.WHITE
            else Piece.BLACK_KING)
    for row in range(8):
        for column in range(8):
            pos = Coordinate(row, column)
            if piece_at(game.board, pos) == king:
                return is_attacked(game, pos, checked_player)


def is_check_mate_for_player(game, player):
    pieces = (WHITE_PIECES
              if player == Player.WHITE
              else BLACK_PIECES)

    for row in range(8):
        for column in range(8):
            pos = Coordinate(row, column)
            if piece_at(game.board, pos) in pieces:
                if len(destinations(game, pos)) > 0:
                    return False
    return True


def is_attacked(game, pos, attacked_player):
    attacker_pieces = (WHITE_PIECES
                       if attacked_player == Player.BLACK
                       else BLACK_PIECES)
    for row in range(8):
        for column in range(8):
            coord = Coordinate(row, column)
            piece = piece_at(game.board, coord)
            if (piece in attacker_pieces and
                    pos in destinations(game, coord, offensive_only=True)):
                return True


def destinations(game, src, offensive_only=False):
    """
    offensive_only means to get the tiles the
    piece at src can attack in the game
    """
    board = game.board
    piece = board[src.row][src.column]
    allowed_destinations = []

    if piece == Piece.WHITE_PAWN:
        up_middle = Coordinate(src.row - 1, src.column)
        up_left = Coordinate(src.row - 1, src.column - 1)
        up_right = Coordinate(src.row - 1, src.column + 1)
        if offensive_only:
            allowed_destinations.append(up_left)
            allowed_destinations.append(up_right)
        else:
            if up_middle.inside_board():
                if board[up_middle.row][up_middle.column] == Piece.NONE:
                    allowed_destinations.append(up_middle)
            if up_left.inside_board():
                if board[up_left.row][up_left.column] != Piece.NONE:
                    allowed_destinations.append(up_left)
            if up_right.inside_board():
                if board[up_right.row][up_right.column] != Piece.NONE:
                    allowed_destinations.append(up_right)
            # double step
            if (src.row == 6):
                double_step_coord = src.up(2)
                if (piece_at(board, double_step_coord) == Piece.NONE and
                        piece_at(board, src.up()) == Piece.NONE):
                    allowed_destinations.append(double_step_coord)

    if piece == Piece.BLACK_PAWN:
        down_middle = Coordinate(src.row + 1, src.column)
        down_left = Coordinate(src.row + 1, src.column - 1)
        down_right = Coordinate(src.row + 1, src.column + 1)
        if offensive_only:
            allowed_destinations.append(down_left)
            allowed_destinations.append(down_right)
        else:
            if down_middle.inside_board():
                if board[down_middle.row][down_middle.column] == Piece.NONE:
                    allowed_destinations.append(down_middle)
            if down_left.inside_board():
                if board[down_left.row][down_left.column] != Piece.NONE:
                    allowed_destinations.append(down_left)
            if down_right.inside_board():
                if board[down_right.row][down_right.column] != Piece.NONE:
                    allowed_destinations.append(down_right)
            # double step
            if (src.row == 1):
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

        # castling
        if not offensive_only:
            if (piece == Piece.WHITE_KING and
                    game.state.allow_castling_white_king):
                if (game.state.allow_castling_left_white_rook and
                    not is_attacked(game, src, Player.WHITE) and
                    not is_attacked(game, src.left(1), Player.WHITE) and
                    not is_attacked(game, src.left(2), Player.WHITE) and
                    empty_at(game.board, src.left(1)) and
                    empty_at(game.board, src.left(2)) and
                        empty_at(game.board, src.left(3))):
                    allowed_destinations.append(src.left(2))
                if (game.state.allow_castling_right_white_rook and
                    not is_attacked(game, src, Player.WHITE) and
                    not is_attacked(game, src.right(1), Player.WHITE) and
                    not is_attacked(game, src.right(2), Player.WHITE) and
                    empty_at(game.board, src.right(1)) and
                        empty_at(game.board, src.right(2))):
                    allowed_destinations.append(src.right(2))
            elif (piece == Piece.BLACK_KING and
                  game.state.allow_castling_black_king):
                if (game.state.allow_castling_left_black_rook and
                    not is_attacked(game, src, Player.BLACK) and
                    not is_attacked(game, src.left(1), Player.BLACK) and
                    not is_attacked(game, src.left(2), Player.BLACK) and
                    empty_at(game.board, src.left(1)) and
                    empty_at(game.board, src.left(2)) and
                        empty_at(game.board, src.left(3))):
                    allowed_destinations.append(src.left(2))
                if (game.state.allow_castling_right_black_rook and
                    not is_attacked(game, src, Player.BLACK) and
                    not is_attacked(game, src.right(1), Player.BLACK) and
                    not is_attacked(game, src.right(2), Player.BLACK) and
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
            allowed_destinations.append(Coordinate(src.row, left))
            if board[src.row][left] != Piece.NONE:
                break
        for right in range(src.column + 1, 8, 1):
            allowed_destinations.append(Coordinate(src.row, right))
            if board[src.row][right] != Piece.NONE:
                break
        for down in range(src.row + 1, 8, 1):
            allowed_destinations.append(Coordinate(down, src.column))
            if board[down][src.column] != Piece.NONE:
                break
        for up in range(src.row - 1, -1, -1):
            allowed_destinations.append(Coordinate(up, src.column))
            if board[up][src.column] != Piece.NONE:
                break
        allowed_destinations += diagonal_moves(board, src)

    if offensive_only:
        return allowed_destinations
    else:
        return [
            coord for coord in allowed_destinations
            if is_valid(game, src, coord)]

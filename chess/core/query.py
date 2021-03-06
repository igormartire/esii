from chess.core.models import Coordinate, Piece, Player, Color
from chess.core.utils import (BLACK_PIECES, WHITE_PIECES,
                              initial_board, piece_at, empty_at,
                              remaining_pieces, color_by_pos,
                              get_piece_coordinate)
from chess.core.moving import move
from chess.core.coloring import color_board
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
    king_pos = get_piece_coordinate(game.board, king)
    if (king_pos is not None):
        return is_attacked(game, king_pos, checked_player)


def is_checkmate_for_player(game, player):
    pieces = (WHITE_PIECES
              if player == Player.WHITE
              else BLACK_PIECES)

    for row in range(8):
        for column in range(8):
            pos = Coordinate(row, column)
            if piece_at(game.board, pos) in pieces:
                if len(destinations(game, pos)) > 0:
                    return False
    # checkmate only when check and also no possible moves
    return is_check_for_player(game, player)


def is_stalemate_for_player(game, player):
    pieces = (WHITE_PIECES
              if player == Player.WHITE
              else BLACK_PIECES)

    for row in range(8):
        for column in range(8):
            pos = Coordinate(row, column)
            if piece_at(game.board, pos) in pieces:
                if len(destinations(game, pos)) > 0:
                    return False
    # stalemate only when not in check but no possible moves
    return not is_check_for_player(game, player)


def is_impossible_checkmate(game):
    king_versus_king = False
    king_and_bishop_versus_king = False
    king_and_knight_versus_king = False
    king_and_bishop_versus_king_and_bishop_on_same_color = False
    remaining_white_pieces = remaining_pieces(game.board, Color.WHITE)
    remaining_black_pieces = remaining_pieces(game.board, Color.BLACK)
    if len(remaining_white_pieces) > 2 or len(remaining_black_pieces) > 2:
        return False
    if len(remaining_white_pieces) == 1 and len(remaining_black_pieces) == 1:
        king_versus_king = True
    elif (len(remaining_white_pieces) == 1 and
          set(remaining_black_pieces) == set([Piece.BLACK_KING,
                                              Piece.BLACK_BISHOP])):
        king_and_bishop_versus_king = True
    elif (len(remaining_black_pieces) == 1 and
          set(remaining_white_pieces) == set([Piece.WHITE_KING,
                                              Piece.WHITE_BISHOP])):
        king_and_bishop_versus_king = True
    elif (len(remaining_white_pieces) == 1 and
          set(remaining_black_pieces) == set([Piece.BLACK_KING,
                                              Piece.BLACK_KNIGHT])):
        king_and_knight_versus_king = True
    elif (len(remaining_black_pieces) == 1 and
          set(remaining_white_pieces) == set([Piece.WHITE_KING,
                                              Piece.WHITE_KNIGHT])):
        king_and_knight_versus_king = True
    elif (set(remaining_white_pieces) == set([Piece.WHITE_KING,
                                              Piece.WHITE_BISHOP]) and
          set(remaining_black_pieces) == set([Piece.BLACK_KING,
                                              Piece.BLACK_BISHOP])):
        white_bishop_pos = get_piece_coordinate(game.board, Piece.WHITE_BISHOP)
        black_bishop_pos = get_piece_coordinate(game.board, Piece.BLACK_BISHOP)
        color_white_bishop_on = color_by_pos(white_bishop_pos)
        color_black_bishop_on = color_by_pos(black_bishop_pos)
        king_and_bishop_versus_king_and_bishop_on_same_color = (
            color_white_bishop_on == color_black_bishop_on)

    return (king_versus_king or
            king_and_bishop_versus_king or
            king_and_knight_versus_king or
            king_and_bishop_versus_king_and_bishop_on_same_color)


def is_attacked(game, pos, attacked_player):
    attacker_pieces = (WHITE_PIECES
                       if attacked_player == Player.BLACK
                       else BLACK_PIECES)
    for row in range(8):
        for column in range(8):
            coord = Coordinate(row, column)
            piece = piece_at(game.board, coord)
            if (piece in attacker_pieces and
                    pos in destinations(game, coord,
                                        all_and_only_offensive=True)):
                return True


def destinations(game, src, all_and_only_offensive=False):
    """
    all_and_only_offensive means to get the tiles the
    piece at src can attack in the game without
    considering checkmates
    """
    board = game.board
    piece = board[src.row][src.column]
    allowed_destinations = []

    if piece == Piece.WHITE_PAWN:
        up_middle = Coordinate(src.row - 1, src.column)
        up_left = Coordinate(src.row - 1, src.column - 1)
        up_right = Coordinate(src.row - 1, src.column + 1)
        if all_and_only_offensive:
            allowed_destinations.append(up_left)
            allowed_destinations.append(up_right)
        else:
            if up_middle.inside_board():
                if board[up_middle.row][up_middle.column] == Piece.NONE:
                    allowed_destinations.append(up_middle)
            if up_left.inside_board():
                if ((board[up_left.row][up_left.column] != Piece.NONE) or
                    (game.state.en_passant_destination is not None and
                     up_left == game.state.en_passant_destination)):
                    allowed_destinations.append(up_left)
            if up_right.inside_board():
                if (board[up_right.row][up_right.column] != Piece.NONE or
                    (game.state.en_passant_destination is not None and
                     up_right == game.state.en_passant_destination)):
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
        if all_and_only_offensive:
            allowed_destinations.append(down_left)
            allowed_destinations.append(down_right)
        else:
            if down_middle.inside_board():
                if board[down_middle.row][down_middle.column] == Piece.NONE:
                    allowed_destinations.append(down_middle)
            if down_left.inside_board():
                if (board[down_left.row][down_left.column] != Piece.NONE or
                    (game.state.en_passant_destination is not None and
                     down_left == game.state.en_passant_destination)):
                    allowed_destinations.append(down_left)
            if down_right.inside_board():
                if (board[down_right.row][down_right.column] != Piece.NONE or
                    (game.state.en_passant_destination is not None and
                     down_right == game.state.en_passant_destination)):
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
        if not all_and_only_offensive:
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
        allowed_destinations = straight_moves(board, src)

    if piece == Piece.WHITE_BISHOP or piece == Piece.BLACK_BISHOP:
        allowed_destinations = diagonal_moves(board, src)

    if piece == Piece.WHITE_QUEEN or piece == Piece.BLACK_QUEEN:
        allowed_destinations = straight_moves(board, src).union(
            diagonal_moves(board, src))

    if all_and_only_offensive:
        return allowed_destinations
    else:
        return [dest for dest in allowed_destinations
                if is_valid(game, src, dest)]


def straight_moves(board, src):
    moves = set()

    # pra esquerda
    for left in range(src.column - 1, -1, -1):
        moves.add(Coordinate(src.row, left))
        if board[src.row][left] != Piece.NONE:
            break

    # pra direita
    for right in range(src.column + 1, 8, 1):
        moves.add(Coordinate(src.row, right))
        if board[src.row][right] != Piece.NONE:
            break

    # pra baixo
    for down in range(src.row + 1, 8, 1):
        moves.add(Coordinate(down, src.column))
        if board[down][src.column] != Piece.NONE:
            break

    # pra cima
    for up in range(src.row - 1, -1, -1):
        moves.add(Coordinate(up, src.column))
        if board[up][src.column] != Piece.NONE:
            break

    return moves


def diagonal_moves(board, src):
    moves = set()

    # diagonal pra cima e pra esquerda
    for i in range(1, min(src.row, src.column) + 1):
        pos = Coordinate(src.row - i, src.column - i)
        moves.add(pos)
        if board[pos.row][pos.column] != Piece.NONE:
            break

    # diagonal pra cima e pra direita
    for i in range(1, min(src.row, 7 - src.column) + 1):
        pos = Coordinate(src.row - i, src.column + i)
        moves.add(pos)
        if board[pos.row][pos.column] != Piece.NONE:
            break

    # diagonal pra baixo e pra esquerda
    for i in range(1, min(7 - src.row, src.column) + 1):
        pos = Coordinate(src.row + i, src.column - i)
        moves.add(pos)
        if board[pos.row][pos.column] != Piece.NONE:
            break

    # diagonal pra baixo e pra direita
    for i in range(1, min(7 - src.row, 7 - src.column) + 1):
        pos = Coordinate(src.row + i, src.column + i)
        moves.add(pos)
        if board[pos.row][pos.column] != Piece.NONE:
            break

    return moves

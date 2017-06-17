from chess.core.models import Coordinate, Piece, Player, Color
from chess.core.utils import (BLACK_PIECES, WHITE_PIECES,
                              piece_at, remaining_pieces, color_by_pos,
                              get_piece_coordinate)
from chess.core.destinations import destinations, is_check_for_player


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

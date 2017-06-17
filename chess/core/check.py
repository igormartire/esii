from chess.core.destinations import destinations
from chess.core.utils import get_piece_coordinate, piece_at
from chess.core.models import Coordiante, Piece, Player


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

    # return False if there is any possible move for player
    for row in range(8):
        for column in range(8):
            pos = Coordinate(row, column)
            if piece_at(game.board, pos) in pieces:
                if len(destinations(game, pos)) > 0:
                    return False

    # checkmate only when check and also no possible moves
    return is_check_for_player(game, player)


def is_attacked(game, pos, attacked_player):
    attacker_pieces = (WHITE_PIECES
                       if attacked_player == Player.BLACK
                       else BLACK_PIECES)

    # returns true if pos can be attacked by any piece
    for row in range(8):
        for column in range(8):
            coord = Coordinate(row, column)
            piece = piece_at(game.board, coord)
            if (piece in attacker_pieces and
                    pos in destinations(game, coord,
                                        all_and_only_offensive=True)):
                return True

    return False

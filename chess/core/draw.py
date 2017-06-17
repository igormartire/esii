from chess.core.models import Coordinate, Piece, Player, Color
from chess.core.utils import (BLACK_PIECES, WHITE_PIECES,
                              piece_at, remaining_pieces, color_by_pos,
                              get_piece_coordinate)


def threefold_repetition(game, src, dest):
    if piece_at(game.board, src) in [Piece.WHITE_PAWN, Piece.BLACK_PAWN]:
        # it is impossible to repeat a board after a pawn movement
        game.clear_threefold_history()
    elif piece_at(game.board, dest) != Piece.NONE:
        # it is impossible to repeat a board after a capture
        game.clear_threefold_history()
    else:
        repetition_count = 1  # this current state
        game_history = game.get_threefold_history()
        for previous_game in game_history:
            if game.is_identical_to(previous_game):
                repetition_count += 1
        if repetition_count >= 3:
            game.draw_allowed_callback()
    game.add_to_history(copy.deepcopy(game))


def fifty_move_rule(game, src, dest):
    piece = piece_at(game.board, src)
    if (piece not in [Piece.WHITE_PAWN, Piece.BLACK_PAWN] and
            piece_at(game.board, dest) == Piece.NONE):
        piece_color = Color.WHITE if piece in WHITE_PIECES else Color.BLACK
        game.fifty_move_rule_count[piece_color] += 1
        if (game.fift_move_rule_count[Color.WHITE] >= 50 and
                game.fift_move_rule_count[Color.BLACK] >= 50):
            game.draw_allowed_callback()
    else:
        game.fift_move_rule_count[piece_color] = 0

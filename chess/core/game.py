from chess.core.utils import initial_board


class Game:
    def __init__(self):
        self.board = initial_board()
        self.state = GameState()
        self.draw_allowed_callback = None

    def register_draw_allowed_callback(callback):
        self.draw_allowed_callback = callback


class GameState:
    def __init__(self):
        self.allow_castling_white_king = True
        self.allow_castling_left_white_rook = True
        self.allow_castling_right_white_rook = True
        self.allow_castling_black_king = True
        self.allow_castling_left_black_rook = True
        self.allow_castling_right_black_rook = True
        self.en_passant_destination = None

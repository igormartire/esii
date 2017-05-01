from enum import Enum, unique

class Coordinate:
    def __init__(self, row, column):
        self.row = row
        self.column = column

@unique
class Color(Enum):
    BLACK = 0
    WHITE = 1
    GREEN = 2
    RED = 3

@unique
class Piece(Enum):
    NONE = '.'
    WHITE_PAWN = 'P'
    WHITE_BISHOP = 'B'
    WHITE_KNIGHT = 'N'
    WHITE_ROOK = 'R'
    WHITE_QUEEN = 'Q'
    WHITE_KING = 'K'
    BLACK_PAWN = 'p'
    BLACK_BISHOP = 'b'
    BLACK_KNIGHT = 'n'
    BLACK_ROOK = 'r'
    BLACK_QUEEN = 'q'
    BLACK_KING = 'k'
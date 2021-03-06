from enum import Enum, unique


class Coordinate:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    @staticmethod
    def matrix_to_coordinates(matrix):
        coordinates = []
        for row in matrix:
            for column in row:
                coordinates[row][column] = Coordinate(row, column)

        return coordinates

    def inside_board(self):
        if self.row < 0 or self.row > 7 or self.column < 0 or self.column > 7:
            return False
        return True

    def __key(self):
        return self.row, self.column

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        return self.__key() == other.__key()

    def __repr__(self):
        return str(self.__key())

    def up(self, n=1):
        return Coordinate(self.row - n, self.column)

    def down(self, n=1):
        return Coordinate(self.row + n, self.column)

    def left(self, n=1):
        return Coordinate(self.row, self.column - n)

    def right(self, n=1):
        return Coordinate(self.row, self.column + n)


@unique
class Color(Enum):
    BLACK = 0
    WHITE = 1
    GREEN = 2
    RED = 3
    BLACK_RGB = (100, 100, 100)
    WHITE_RGB = (230, 230, 230)
    GREEN_RGB = (50, 200, 50)
    RED_RGB = (200, 50, 50)

    @property
    def rgb(self):
        if self == Color.BLACK:
            return (100, 100, 100)
        if self == Color.WHITE:
            return (230, 230, 230)
        if self == Color.GREEN:
            return (50, 200, 50)
        if self == Color.RED:
            return (200, 50, 50)


@unique
class Player(Enum):
    BLACK = 0
    WHITE = 1


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

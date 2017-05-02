from enum import Enum, unique


class Coordinate:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    @classmethod
    def matrix_to_coordinates(cls, matrix):
        coordinates = []
        for row in matrix:
            for column in row:
                coordinates[row][column] = Coordinate(row, column)

        return coordinates

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def __repr__(self):
        return "(" + str(self.row) + ", " + str(self.column) + ")"


class Board:
    def __init__(self, cells_matrix):
        self.matrix = cells_matrix
        self.coordinates = Coordinate.matrix_to_coordinates(self.matrix)
        self.width = len(cells_matrix[0])
        self.height = len(cells_matrix)


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

    @classmethod
    def get_rgb(cls, code):
        if code == 0:
            return Color.BLACK_RGB.value
        if code == 1:
            return Color.WHITE_RGB.value
        if code == 2:
            return Color.GREEN_RGB.value
        if code == 3:
            return Color.RED_RGB.value


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




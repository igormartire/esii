from chess.core.models import Piece, Coordinate
import copy


def move(board, src, dest):
    board = copy.deepcopy(board)
    piece = board[src.row][src.column]
    board[src.row][src.column] = Piece.NONE
    board[dest.row][dest.column] = piece
    return board


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

    return set(moves)

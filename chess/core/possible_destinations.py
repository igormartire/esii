from .models import Coordinate, Piece
from .utils import BLACK_PIECES, WHITE_PIECES, INITIAL_BOARD


# TODO: mover movimentação para funções
# TODO: fazer movimentações retornarem um set
# TODO: adicionar testes (basear-se em moving_test)

def is_valid(piece, dest_coord, chess_board):
    print(dest_coord)
    if not dest_coord.inside_board:
        return False

    # TODO: fazer isso decentemente...
    if dest_coord.row >= 0 and dest_coord.row < 8 and dest_coord.column >= 0 and dest_coord.column < 8:
        dest_piece = chess_board[dest_coord.row][dest_coord.column]
        if dest_piece != Piece.NONE:
            if piece in WHITE_PIECES and dest_piece in WHITE_PIECES:
                return False
            if piece in BLACK_PIECES and dest_piece in BLACK_PIECES:
                return False
        return True
    return False


def diagonal_moves(board, src):
    moves = set()

    #diagonal pra cima e pra esquerda
    for i in range(1, min(src.row, src.column) + 1):
        pos = Coordinate(src.row - i, src.column - i)
        moves.add(pos)
        if board[pos.row][pos.column] != Piece.NONE:
            break

    #diagonal pra cima e pra direita
    for i in range(1, min(src.row, 7 - src.column) + 1):
        pos = Coordinate(src.row - i, src.column + i)
        moves.add(pos)
        if board[pos.row][pos.column] != Piece.NONE:
            break

    #diagonal pra baixo e pra esquerda
    for i in range(1, min(7 - src.row, src.column) + 1):
        pos = Coordinate(src.row + i, src.column - i)
        moves.add(pos)
        if board[pos.row][pos.column] != Piece.NONE:
            break

    #diagonal pra baixo e pra direita
    for i in range(1, min(7 - src.row, 7 - src.column) + 1):
        pos = Coordinate(src.row + i, src.column + i)
        moves.add(pos)
        if board[pos.row][pos.column] != Piece.NONE:
            break

    return set(moves)


def destinations(origin_coord, chess_board):
    piece = chess_board[origin_coord.row][origin_coord.column]
    allowed_destinations = []

    if piece == Piece.WHITE_PAWN:
        allowed_destinations = [
            Coordinate(origin_coord.row - 1, origin_coord.column)
        ]

    if piece == Piece.BLACK_PAWN:
        allowed_destinations = [
            Coordinate(origin_coord.row + 1, origin_coord.column)
        ]

    if piece == Piece.WHITE_KNIGHT or piece == Piece.BLACK_KNIGHT:
        allowed_destinations = [
            # Up
            Coordinate(origin_coord.row - 2, origin_coord.column - 1),
            Coordinate(origin_coord.row - 2, origin_coord.column + 1),
            Coordinate(origin_coord.row - 1, origin_coord.column - 2),
            Coordinate(origin_coord.row - 1, origin_coord.column + 2),
            # Down
            Coordinate(origin_coord.row + 2, origin_coord.column - 1),
            Coordinate(origin_coord.row + 2, origin_coord.column + 1),
            Coordinate(origin_coord.row + 1, origin_coord.column - 2),
            Coordinate(origin_coord.row + 1, origin_coord.column + 2),
        ]

    if piece == Piece.WHITE_KING or piece == Piece.BLACK_KING:
        allowed_destinations = [
            Coordinate(origin_coord.row - 1, origin_coord.column - 1),
            Coordinate(origin_coord.row - 1, origin_coord.column - 0),
            Coordinate(origin_coord.row - 1, origin_coord.column + 1),
            Coordinate(origin_coord.row - 0, origin_coord.column - 1),
            Coordinate(origin_coord.row - 0, origin_coord.column + 1),
            Coordinate(origin_coord.row + 1, origin_coord.column - 1),
            Coordinate(origin_coord.row + 1, origin_coord.column - 0),
            Coordinate(origin_coord.row + 1, origin_coord.column + 1),
        ]

    if piece == Piece.WHITE_ROOK or piece == Piece.BLACK_ROOK:
        for left in range(origin_coord.column-1, -1, -1):
            allowed_destinations += [
                Coordinate(origin_coord.row, left)
            ]
            if chess_board[origin_coord.row][left] != Piece.NONE:
                break
        for right in range(origin_coord.column+1, 8, 1):
            allowed_destinations += [
                Coordinate(origin_coord.row, right)
            ]
            if chess_board[origin_coord.row][right] != Piece.NONE:
                break
        for down in range(origin_coord.row+1, 8, 1):
            allowed_destinations += [
                Coordinate(down, origin_coord.column)
            ]
            if chess_board[down][origin_coord.column] != Piece.NONE:
                break
        for up in range(origin_coord.row-1, -1, -1):
            allowed_destinations += [
                Coordinate(up, origin_coord.column)
            ]
            if chess_board[up][origin_coord.column] != Piece.NONE:
                break

    if piece == Piece.WHITE_BISHOP or piece == Piece.BLACK_BISHOP:
        allowed_destinations = diagonal_moves(chess_board, origin_coord)

    if piece == Piece.WHITE_QUEEN or piece == Piece.BLACK_QUEEN:
        for left in range(origin_coord.column-1, -1, -1):
            allowed_destinations += [
                Coordinate(origin_coord.row, left)
            ]
            if chess_board[origin_coord.row][left] != Piece.NONE:
                break
        for right in range(origin_coord.column+1, 8, 1):
            allowed_destinations += [
                Coordinate(origin_coord.row, right)
            ]
            if chess_board[origin_coord.row][right] != Piece.NONE:
                break
        for down in range(origin_coord.row+1, 8, 1):
            allowed_destinations += [
                Coordinate(down, origin_coord.column)
            ]
            if chess_board[down][origin_coord.column] != Piece.NONE:
                break
        for up in range(origin_coord.row-1, -1, -1):
            allowed_destinations += [
                Coordinate(up, origin_coord.column)
            ]
            if chess_board[up][origin_coord.column] != Piece.NONE:
                break
        # diagonal pra cima e pra esquerda
        for i in range(min(origin_coord.row, origin_coord.column)):
            pos = Coordinate(origin_coord.row - i, origin_coord.column - i)
            allowed_destinations.append(pos)
            if chess_board[pos.row][pos.column] != Piece.NONE:
                break

        # diagonal pra cima e pra direita
        for i in range(min(origin_coord.row, 7 - origin_coord.column)):
            pos = Coordinate(origin_coord.row - i, origin_coord.column + i)
            allowed_destinations.append(pos)
            if chess_board[pos.row][pos.column] != Piece.NONE:
                break

        # diagonal pra baixo e pra esquerda
        for i in range(min(7 - origin_coord.row, origin_coord.column)):
            pos = Coordinate(origin_coord.row + i, origin_coord.column - i)
            allowed_destinations.append(pos)
            if chess_board[pos.row][pos.column] != Piece.NONE:
                break

        # diagonal pra baixo e pra direita
        for i in range(min(7 - origin_coord.row, 7 - origin_coord.column)):
            pos = Coordinate(origin_coord.row + i, origin_coord.column + i)
            allowed_destinations.append(pos)
            if chess_board[pos.row][pos.column] != Piece.NONE:
                break

    valid_destinations = [
        coord for coord in allowed_destinations
        if is_valid(piece, coord, chess_board)]

    return valid_destinations

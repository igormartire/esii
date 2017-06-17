from chess.core.models import Piece, Coordinate
import copy


def move(game, src, dest, promotion_callback=None):
    board = game.board
    piece = board[src.row][src.column]

    castling(game, src, dest)

    board[src.row][src.column] = Piece.NONE
    board[dest.row][dest.column] = piece

    promotion(game, dest, promotion_callback)
    en_passant(game, src, dest)


def en_passant(game, src, dest):
    board = game.board
    piece = board[dest.row][dest.column]

    # handle previous en passant
    if game.state.en_passant_destination is not None:
        if dest == game.state.en_passant_destination:
            if piece == Piece.WHITE_PAWN:
                board[dest.row + 1][dest.column] = Piece.NONE
            else:  # black pawn did the en passant
                board[dest.row - 1][dest.column] = Piece.NONE

        # the en passant opportunity is now over
        game.state.en_passant_destination = None

    # verify if new en passant
    if piece == Piece.WHITE_PAWN:
        if abs(src.row - dest.row) == 2:  # double step
            game.state.en_passant_destination = dest.down()
    elif piece == Piece.BLACK_PAWN:
        if abs(src.row - dest.row) == 2:  # double step
            game.state.en_passant_destination = dest.up()


def promotion(game, dest, promotion_callback):
    board = game.board
    piece = board[dest.row][dest.column]

    promoted_piece = None
    if piece == Piece.WHITE_PAWN and dest.row == 0:
        if promotion_callback is None:
            promoted_piece = Piece.WHITE_QUEEN
        else:
            promoted_piece = promotion_callback(board)
    elif piece == Piece.BLACK_PAWN and dest.row == 7:
        promoted_piece = Piece.BLACK_QUEEN

    if promoted_piece is not None:
        board[dest.row][dest.column] = promoted_piece


def castling(game, src, dest):
    board = game.board
    piece = board[src.row][src.column]

    if (piece == Piece.WHITE_KING and
        src == Coordinate(7, 4) and
            dest == Coordinate(7, 6)):
        board[7][5] = Piece.WHITE_ROOK
        board[7][7] = Piece.NONE
    elif (piece == Piece.WHITE_KING and
          src == Coordinate(7, 4) and
          dest == Coordinate(7, 2)):
        board[7][3] = Piece.WHITE_ROOK
        board[7][0] = Piece.NONE
    elif (piece == Piece.BLACK_KING and
          src == Coordinate(0, 4) and
          dest == Coordinate(0, 6)):
        board[0][5] = Piece.BLACK_ROOK
        board[0][0] = Piece.NONE
    elif (piece == Piece.BLACK_KING and
          src == Coordinate(0, 4) and
          dest == Coordinate(0, 2)):
        board[0][3] = Piece.BLACK_ROOK
        board[0][0] = Piece.NONE

    if (piece == Piece.WHITE_KING and
            game.state.allow_castling_white_king):
        game.state.allow_castling_white_king = False
    elif (piece == Piece.WHITE_ROOK and
          src == Coordinate(7, 0) and
          game.state.allow_castling_left_white_rook):
        game.state.allow_castling_left_white_rook = False
    elif (piece == Piece.WHITE_ROOK and
          src == Coordinate(7, 7) and
          game.state.allow_castling_right_white_rook):
        game.state.allow_castling_right_white_rook = False
    elif (piece == Piece.BLACK_KING and
          game.state.allow_castling_black_king):
        game.state.allow_castling_black_king = False
    elif (piece == Piece.BLACK_ROOK and
          src == Coordinate(0, 0) and
          game.state.allow_castling_left_black_rook):
        game.state.allow_castling_left_black_rook = False
    elif (piece == Piece.BLACK_ROOK and
          src == Coordinate(0, 7) and
          game.state.allow_castling_right_black_rook):
        game.state.allow_castling_right_black_rook = False


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

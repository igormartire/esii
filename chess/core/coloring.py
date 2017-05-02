from chess.core.models import Color, Piece


# Example:
# colored_board = color_board(
#   board,
#   [models.Coordinate(1,1), models.Coordinate(3,5)]
# )
def color_board(board, possible_destinations):
    # TODO: verificar se isso é mesmo necessário ou se estamos dando voltas a toa
    B = Color.BLACK.value
    W = Color.WHITE.value

    colored_board = [[W, B, W, B, W, B, W, B],
                     [B, W, B, W, B, W, B, W],
                     [W, B, W, B, W, B, W, B],
                     [B, W, B, W, B, W, B, W],
                     [W, B, W, B, W, B, W, B],
                     [B, W, B, W, B, W, B, W],
                     [W, B, W, B, W, B, W, B],
                     [B, W, B, W, B, W, B, W]]

    for dest in possible_destinations:
        if board[dest.row][dest.column] != Piece.NONE:
            #print(board[dest.row][dest.column])
            colored_board[dest.row][dest.column] = Color.RED.value
        else:
            colored_board[dest.row][dest.column] = Color.GREEN.value

    return colored_board

from chess.core.models import Coordinate
from chess.core.moving import move
from chess.core.possible_destinations import destinations
from chess.ai.score import score_board
from chess.core.utils import BLACK_PIECES
import copy


def greedy_move(game):
    best_move = None
    best_value = -9999
    for row in range(8):
        for column in range(8):
            piece = game.board[row][column]
            if piece in BLACK_PIECES:
                src = Coordinate(row, column)
                dests = destinations(game, src)
                for dest in dests:
                    possible_game = copy.deepcopy(game)
                    print(possible_game.board)
                    print()
                    move(possible_game, src, dest)
                    possible_value = score_board(possible_game.board)
                    if possible_value > best_value:
                        best_value = possible_value
                        best_move = (src, dest)
    return best_move

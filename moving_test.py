# from chess.core.moving import move
# from chess.core.models import Game, Coordinate, Piece
# import mock

# def do_nothing():
#     pass

# def test_move():
#     @mock.patch('chess.core.castling', side_effect=do_nothing)
#     @mock.patch('chess.core.promotion', side_effect=do_nothing)
#     @mock.patch('chess.core.en_passant', side_effect=do_nothing)
#     game = Game()

#     assert(game.board[7][0] == Piece.WHITE_ROOK)
#     assert(game.board[7][4] == Piece.WHITE_KING)

#     move(game, Coordinate(7, 0), Coordinate(7, 4))

#     assert(game.board[7][0] == Piece.NONE)
#     assert(game.board[7][4] == Piece.WHITE_ROOK)

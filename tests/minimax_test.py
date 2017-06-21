from chess.ai.minimax import Minimax
from chess.core.models import Piece, Coordinate
from chess.core.utils import initial_board
from chess.core.game import Game
from chess.ai.state import State

def test_minimax_depth_2():
	game = Game()
	
	game.board = initial_board()
	
	game.board[2][0] = Piece.BLACK_KNIGHT
	game.board[0][1] = Piece.NONE
	
	game.board[4][1] = Piece.WHITE_PAWN
	game.board[6][1] = Piece.NONE
	game.board[5][2] = Piece.WHITE_PAWN
	game.board[6][2] = Piece.NONE
	game.board[4][3] = Piece.WHITE_PAWN
	game.board[6][3] = Piece.NONE
	game.board[4][4] = Piece.WHITE_PAWN
	game.board[6][4] = Piece.NONE
	
	difficulty = "medium"
	value = 0
	state = State(game, value)
	cpu = Minimax(state, difficulty)
	vet = cpu.cpu_move()
	
	position = (vet[1], vet[2])

	assert position == (Coordinate(2, 0), Coordinate(0, 1))


def test_minimax_depth_3():
	game = Game()
	
	game.board = initial_board()
	
	game.board[2][0] = Piece.BLACK_KNIGHT
	game.board[0][1] = Piece.NONE
	
	game.board[4][1] = Piece.WHITE_PAWN
	game.board[6][1] = Piece.NONE
	game.board[5][2] = Piece.WHITE_PAWN
	game.board[6][2] = Piece.NONE
	game.board[4][3] = Piece.WHITE_PAWN
	game.board[6][3] = Piece.NONE
	game.board[4][4] = Piece.WHITE_PAWN
	game.board[6][4] = Piece.NONE
	
	difficulty = "hard"
	value = 0
	state = State(game, value)
	cpu = Minimax(state, difficulty)
	vet = cpu.cpu_move()
	
	position = (vet[1], vet[2])

	assert position == (Coordinate(0, 0), Coordinate(0, 1))
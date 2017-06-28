from chess.ai.minimax import Minimax
from chess.core.models import Piece, Coordinate
from chess.core.utils import initial_board
from chess.core.game import Game
from chess.ai.state import State
from chess.core.utils import _, K, k, Q, q, R, r, N, n, B, b, P, p


def test_minimax_depth_2():
    game = Game()
    game.board = [[_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [n, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, P, _, _, _, _, _, _],
                  [P, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, _, _]]
    difficulty = "medium"
    value = 0
    state = State(game, value)
    cpu = Minimax(state, difficulty)
    vet = cpu.cpu_move()
    position = (vet[1], vet[2])
    assert position == (Coordinate(2, 0), Coordinate(0, 1))


def test_minimax_depth_3():
    game = Game()
    game.board = [[_, _, _, _, _, _, _, _],
                  [_, _, _, _, p, _, _, _],
                  [n, _, _, _, P, _, _, _],
                  [_, p, _, _, _, _, _, _],
                  [p, P, _, _, _, _, _, _],
                  [P, _, _, _, _, _, _, _],
                  [_, _, _, _, _, _, P, _],
                  [_, _, _, _, _, _, _, _]]
    difficulty = "hard"
    value = 0
    state = State(game, value)
    cpu = Minimax(state, difficulty)
    vet = cpu.cpu_move()

    position = (vet[1], vet[2])

    assert position == (Coordinate(2, 0), Coordinate(1, 2))


def test_minimax_random():
    game = Game()
    game.board = initial_board()
    difficulty = "medium"
    value = 0
    state = State(game, value)
    cpu = Minimax(state, difficulty)
    movements = []
    for i in range(5):
        vet = cpu.cpu_move()
        movements.append(vet)
    assert diff_movement(movements) is True


def diff_movement(moves):
    for m in moves:
        if moves[0] != m:
            return True
    return False

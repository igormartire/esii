# -*- coding: UTF-8 -*-
# Minimax com poda alpha-beta

from chess.core.models import Coordinate
from random import randint
from chess.core.moving import move
from chess.ai.score import score_board
from chess.core.models import Player
from chess.core.utils import BLACK_PIECES, WHITE_PIECES
from chess.core.query import destinations, is_checkmate_for_player

from copy import deepcopy


class Minimax:
    VICTORY = 10000

    def __init__(self, state, difficulty):
        self.state = state
        self.difficulty = difficulty

    def difficulty_check(self, difficulty):
        depth = 0
        if self.difficulty == "easy":
            depth = 1
        elif self.difficulty == "medium":
            depth = 2
        elif self.difficulty == "hard":
            depth = 3

        return depth

    # Realiza a jogada do PC, devolvendo um array [pos_x, pos_y]
    # com as posições da jogada
    def cpu_move(self):
        return self.max_value(self.state, float('-inf'), float('inf'),
                              self.difficulty_check(self.difficulty))

    # Minimiza a jogada do oponente	(peça branca)
    def min_value(self, state, alfa, beta, depth):
        # o algoritmo para quando chega na profundidade especificada
        # e retorna o valor da ultima jogada e para a recursão
        if self.cutoff_test(depth):
            return [score_board(state.game.board), None, None]

        if is_checkmate_for_player(self.state.game, Player.BLACK):
            return [-self.VICTORY, None]

        v_list = []

        for movement in self.valid_movements(state, WHITE_PIECES):
            v = [float("inf"), None, None]
            source = movement[0]
            destination = movement[1]

            minstate = deepcopy(state)
            # faz a jogada
            move(minstate.game, source, destination)
            # valor da jogada

            # momento em que pega a jogada do adversário
            best_score = self.max_value(minstate, alfa, beta, depth - 1)

            v[0] = best_score[0]
            v[1] = source
            v[2] = destination

            v_list.append(v)

            if v[0] <= alfa:
                if self.random_movement(v_list):
                    return v_list[randint(0, len(v_list) - 1)]

                else:
                    return min(v_list, key=lambda v: v[0])

            beta = min(v[0], beta)

        if len(v_list) == 0:
            return [float('inf'), None, None]

        if self.random_movement(v_list):
            return v_list[randint(0, len(v_list) - 1)]

        else:
            return min(v_list, key=lambda v: v[0])

    # Maximiza a jogada do PC (peça preta)
    def max_value(self, state, alfa, beta, depth):
        # o algoritmo para quando chega na profundidade especificada e
        # retorna o valor da ultima jogada e para a recursão
        if self.cutoff_test(depth):
            return [score_board(state.game.board), None, None]

        if is_checkmate_for_player(self.state.game, Player.WHITE):
            return [self.VICTORY, None]

        v_list = []

        vm = self.valid_movements(state, BLACK_PIECES)
        for movement in vm:
            v = [float("-inf"), None, None]
            source = movement[0]
            destination = movement[1]

            maxstate = deepcopy(state)
            # faz a jogada
            move(maxstate.game, source, destination)

            # momento em que pega a jogada do adversário
            best_score = self.min_value(maxstate, alfa, beta, depth - 1)

            v[0] = best_score[0]
            v[1] = source
            v[2] = destination

            v_list.append(v)

            if v[0] >= beta:
                if self.random_movement(v_list):
                    return v_list[randint(0, len(v_list) - 1)]

                else:
                    return max(v_list, key=lambda v: v[0])

            alfa = max(v[0], alfa)

        if len(v_list) == 0:
            return [float('-inf'), None, None]

        if self.random_movement(v_list):
            return v_list[randint(0, len(v_list) - 1)]

        else:
            return max(v_list, key=lambda v: v[0])

    def valid_movements(self, state, piece_type):
        destinations_list = []

        for row in range(8):
            for column in range(8):
                piece = state.game.board[row][column]
                if piece in piece_type:

                    src = Coordinate(row, column)

                    for dest in destinations(state.game, src):

                        destinations_list.append((src, dest))

        return destinations_list

    def random_movement(self, l):

        for i in l:
            if l[0][0] != i[0]:
                return False

        return True

    def cutoff_test(self, depth):
        return depth == 0

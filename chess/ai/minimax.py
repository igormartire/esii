# -*- coding: UTF-8 -*-
# Minimax com poda alpha-beta

from chess.core.models import Coordinate
import operator
from random import*
from chess.core.moving import move
from chess.core.possible_destinations import destinations
from chess.ai.score import score_board
from chess.core.models import Piece, Player
from chess.core.utils import BLACK_PIECES, WHITE_PIECES
from chess.core.possible_destinations import (destinations,
                                              is_check_for_player,
                                              is_check_mate_for_player)

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

    # Realiza a jogada do PC, devolvendo um array [pos_x, pos_y] com as posições da jogada
    def cpu_move(self):
        return self.max_value(self.state, float('-inf'), float('inf'), self.difficulty_check(self.difficulty))

    # Minimiza a jogada do oponente	(peça branca)
    def min_value(self, state, alfa, beta, depth):
        # o algoritmo para quando chega na profundidade especificada e retorna o valor da ultima jogada e para a recursão
        if self.cutoff_test(depth):
        	return [state.value, None, None]

        if is_check_mate_for_player(self.state.game, Player.BLACK):
            return [-self.VICTORY, None]

        v_list = []

        for movement in self.valid_movements(state, WHITE_PIECES):
            v = [float("inf"), None, None]
            source = movement[0]
            
            minstate = deepcopy(state)
            # faz a jogada
            move(minstate.game, source, movement[1])
            # valor da jogada
            # if (source == Coordinate(4, 6) and movement[1] == Coordinate(3,7)):
                
            v[0] = score_board(minstate.game.board)
                        
            # associa o valor da jogada com o estado atual
            minstate.value = v[0]
                        
            # momento em que pega a jogada do adversário
            m = self.max_value(minstate, alfa, beta, depth - 1)
            
            if m != None:            
                if m[0] > v[0]:
                    v[0] = m[0]
                            
            v[1] = source
            v[2] = movement[1]

            v_list.append(v)
            
            if v[0] <= alfa:
                if self.jogada_aleatoria(v_list):
                    if len(v_list) != 0:
                        return v_list[randint(0, len(v_list) - 1)]
                else:
                    return min(v_list, key=lambda v: v[0])
            
            beta = min(v[0], beta)

        if self.jogada_aleatoria(v_list):
            if len(v_list) != 0:
                return v_list[randint(0, len(v_list) - 1)]
        else:    
            return min(v_list, key=lambda v: v[0])

    # Maximiza a jogada do PC (peça preta)
    def max_value(self, state, alfa, beta, depth):
        # o algoritmo para quando chega na profundidade especificada e retorna o valor da ultima jogada e para a recursão
        if self.cutoff_test(depth):
        	return [state.value, None, None]

        if is_check_mate_for_player(self.state.game, Player.WHITE):
            return [self.VICTORY, None]

        v_list = []
        
        vm = self.valid_movements(state, BLACK_PIECES)
        for movement in vm:
            v = [float("-inf"), None, None]
            source = movement[0]
            maxstate = deepcopy(state)
            # faz a jogada
            move(maxstate.game, source, movement[1])
            # valor da jogada
            v[0] = score_board(maxstate.game.board)
                        
            # associa o valor da jogada com o estado atual
            maxstate.value = v[0]
                        
            # momento em que pega a jogada do adversário
            m = self.min_value(maxstate, alfa, beta, depth - 1)
            
            if m != None:         
                if m[0] < v[0]:
                    v[0] = m[0]
                            
            v[1] = source
            v[2] = movement[1]

            v_list.append(v)
            
            if v[0] >= beta:
                if self.jogada_aleatoria(v_list):
                    if len(v_list) != 0:
                        return v_list[randint(0, len(v_list) - 1)]
                else:
                    return max(v_list, key=lambda v: v[0])
            
            alfa = max(v[0], alfa)
            
        if self.jogada_aleatoria(v_list):
            if len(v_list) != 0:
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

    def jogada_aleatoria(self, l):
        for i in l:
            if l[0][0] != i[0]:
                return False
        return True

    def cutoff_test(self, depth):
        if depth == 0:
            return True

        return False
# -*- coding: UTF-8 -*-
# Minimax com poda alpha-beta

from chess.core.models import Coordinate
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
    VICTORY = 100

    def __init__(self, state):
        self.state = state

    # Realiza a jogada do PC, devolvendo um array [pos_x, pos_y] com as posições da jogada
    def cpu_move(self):
        return self.max_value(self.state, float('-inf'), float('inf'), 4)

    # Minimiza a jogada do oponente	(peça branca)
    def min_value(self, state, alfa, beta, depth):
        # condição de parada da recursão
        if is_check_mate_for_player(self.state.game, Player.BLACK):
            return [self.VICTORY, None]

        # o algoritmo para quando chega na profundidade especificada e retorna o valor da ultima jogada e para a recursão
        if self.cutoff_test(state, depth):
        	return [state.value, None]
        
        v = [float("inf"), None, None]
        v_list = []

        for movement in self.valid_movements(self.state, WHITE_PIECES):
            source = movement[0]
            
            minstate = deepcopy(state)
            # faz a jogada
            move(minstate.game, source, movement[1])
            # valor da jogada
            v[0] = score_board(minstate.game.board)
                        
            # associa o valor da jogada com o estado atual
            state.value = v[0]
                        
            # momento em que pega a jogada do adversário
            m = self.max_value(minstate, alfa, beta, depth - 1)
                        
            if m[0] < v[0]:
                v[0] = m[0]
                        
            v[1] = source
            v[2] = movement[1]

            v_list.append(v)
            print("Min")
            print(min(v_list, key=lambda v: v[0]))
            if v[0] <= alfa:
                return min(v_list, key=lambda v: v[0])
            
            beta = min(v[0], beta)
            
        
        return min(v_list, key=lambda v: v[0])

    # Maximiza a jogada do PC (peça preta)
    def max_value(self, state, alfa, beta, depth):
        # condição de parada da recursão
        if is_check_mate_for_player(self.state.game, Player.WHITE):
            return [self.VICTORY, None]

        # o algoritmo para quando chega na profundidade especificada e retorna o valor da ultima jogada e para a recursão
        if self.cutoff_test(state, depth):
        	return [state.value, None]
        
        v = [float("-inf"), None, None]
        v_list = []
        
        for movement in self.valid_movements(self.state, BLACK_PIECES):
            source = movement[0]
            maxstate = deepcopy(state)
            # faz a jogada
            move(maxstate.game, source, movement[1])
            # valor da jogada
            v[0] = score_board(maxstate.game.board)
                        
            # associa o valor da jogada com o estado atual
            state.value = v[0]
                        
            # momento em que pega a jogada do adversário
            m = self.min_value(maxstate, alfa, beta, depth - 1)
                        
            if m[0] > v[0]:
                v[0] = m[0]
                        
            v[1] = source
            v[2] = movement[1]

            v_list.append(v)
            print("Max")
            print(max(v_list, key=lambda v: v[0]))
            if v[0] >= beta:
                return max(v_list, key=lambda v: v[0])
            
            alfa = max(v[0], alfa)
            
        return max(v_list, key=lambda v: v[0])

    # função de teste da poda do cutoff
    def cutoff_test(self, state, depth):
    	if depth == 0:
    		return 1
    	else:
    		return 0

    	return 0

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
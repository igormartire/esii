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

    def __init__(self, state, game):
        self.state = state
        self.game = game

    # Realiza a jogada do PC, devolvendo um array [pos_x, pos_y] com as posições da jogada
    def cpu_move(self):
        """
            Interessa apenas a jogada e não o seu valor, por isso retorna apenas max_value()[1]
        """
        return self.max_value(self.state, float('-inf'), float('inf'), 5)[1]

    # Minimiza a jogada do oponente	(peça branca)
    def min_value(self, state, alfa, beta, depth):
        # condição de parada da recursão
        if is_check_mate_for_player(self.game, Player.BLACK):
            return [self.VICTORY, None]

        # o algoritmo para quando chega na profundidade especificada e retorna o valor da ultima jogada e para a recursão
        if self.cutoff_test(state, depth):
        	return [state.eval, None]
        
        v = [float("inf"), None]

        for row in range(8):
            for column in range(8):
                piece = state.board[row][column]

                if piece in WHITE_PIECES:

                    src = Coordinate(row, column)
                    for move in destinations(state.game, src, False):
                    	 
                        minstate = deepcopy(state)
                        # faz a jogada
                        minstate.board = move(minstate.game, src, move)
                        # valor da jogada
                        v[0] = score_board(minstate.board)
                        
                        # associa o valor da jogada com o estado atual
                        state.eval = v[0]
                        
                        # momento em que pega a jogada do adversário
                        m = self.max_value(minstate, alfa, beta, depth - 1)
                        
                        if m[0] < v[0]:
                            v[0] = m[0]
                        
                        v[1] = move
                        
                        if v[0] <= alfa:
                            return v
                        beta = min(v[0], beta)
        
        return v

    # Maximiza a jogada do PC (peça preta)
    def max_value(self, state, alfa, beta, depth):
        # condição de parada da recursão
        if is_check_mate_for_player(self.game, Player.WHITE):
            return [self.VICTORY, None]

        # o algoritmo para quando chega na profundidade especificada e retorna o valor da ultima jogada e para a recursão
        if self.cutoff_test(state, depth):
        	return [state.eval, None]
        
        v = [float("-inf"), None]

        for row in range(8):
            for column in range(8):
                piece = state.board[row][column]

                if piece in BLACK_PIECES:

                    src = Coordinate(row, column)
                    for move in destinations(state.game, src, False):

                        maxstate = deepcopy(state)
                        # faz a jogada
                        maxstate.board = move(maxstate.game, src, move)
                        # valor da jogada
                        v[0] = score_board(maxstate.board)
                        
                        # associa o valor da jogada com o estado atual
                        state.eval = v[0]
                        
                        # momento em que pega a jogada do adversário
                        m = self.min_value(maxstate, alfa, beta, depth - 1)
                        
                        if m[0] > v[0]:
                            v[0] = m[0]
                        
                        v[1] = move
                        
                        if v[0] >= beta:
                            return v
                        alfa = max(v[0], alfa)
        
        return v

    # função de teste da poda do cutoff
    def cutoff_test(self, state, depth):
    	if depth == 0:
    		return 1
    	else:
    		return 0

    	return 0


#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chess.core.utils import initial_board
from chess.core.game import Game

class State:
    def __init__(self, board, game, eval):
        self.board = board
        self.game = game
        #valor da jogada
        self.eval = eval

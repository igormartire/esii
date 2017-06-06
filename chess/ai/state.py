#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chess.core.utils import initial_board
from chess.core.game import Game

class State:
    def __init__(self, game, value):
        self.game = game
        #valor da jogada
        self.value = value

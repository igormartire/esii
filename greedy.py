# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Victor"
__date__ = "$30/04/2017 15:21:55$"

import chessai
import move
import possible_moviments

if __name__ == "__main__":

    def greedy(board):
        
        
        boards = []
        evaluations = []

        evaluation = 0

        new_destinations = []

        for i in range(8):
            for j in range(8):
                b = board
                
                piece = b[i][j]
                source = possible_moviments.Coordinate(i, j)    
                
                if (piece == "r") or (piece == "n") or (piece == "b") or (piece == "q") or (piece == "k") or (piece == "p"):
                    
                    new_destinations = possible_moviments.destinations(piece, source, b)
                    
                    for k in range(len(new_destinations)):
                        dest = new_destinations[k]
                        
                        dest_x = dest[0]
                        dest_y = dest[1]
                        
                        move.move(b, source.row, source.column, dest_x, dest_y)

                        evaluation = chessai.evaluation_function(b)

                        boards.append(b)
                        evaluations.append(evaluation)

        return boards[evaluations.index(max(evaluations))]
 
board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
         ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
         ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

greedy(board)

print (board)
                
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Victor"
__date__ = "$09/04/2017 16:22:25$"


if __name__ == "__main__":
    board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], 
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], 
            ['.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.'], 
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], 
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
            ]
    
    def evaluation_function(board):
        sum = 0
        n_R = 0
        n_N = 0
        n_B = 0
        n_Q = 0
        n_K = 0
        n_P = 0
        n_r = 0
        n_n = 0
        n_b = 0
        n_q = 0
        n_k = 0
        n_p = 0
        for i in range(0, 8):
            for j in range(0, 8):
                piece = board[i][j]
                
                if piece == "R":
                   n_R += 1
                elif piece == "N":
                    n_N += 1
                elif piece == "B":
                    n_B += 1
                elif piece == "Q":
                    n_Q += 1
                elif piece == "k":
                    n_K += 1
                elif piece == "P":
                    n_P += 1
                elif piece == "r":
                   n_r += 1
                elif piece == "n":
                    n_n += 1
                elif piece == "b":
                    n_b += 1
                elif piece == "q":
                    n_q += 1
                elif piece == "k":
                    n_k += 1
                elif piece == "p":
                    n_p += 1
        
        sum += 9*(n_Q - n_q) + 5*(n_R - n_r) + 3*(n_B - n_b) + (n_P - n_p)    
        print(sum)
    
    evaluation_function(board)
    
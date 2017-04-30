# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Victor"
__date__ = "$30/04/2017 15:21:55$"

if __name__ == "__main__":
    def greedy(board):
        list = []
        item_list = []
        
        evaluation = 0
        best_evaluation = 0
        
        new_destinations = []
        source = []
        
        for i in range(0, 8):
            for j in range(0, 8):
                piece = board[i][j]
                
                source[0] = i
                source[1] = j
                
                new_destinations = destinations(piece, source)
                
                for k in range(0, len(new_destinations)):
                    dest = new_destinations[k]
                    dest_x = dest[0]
                    dest_y = dest[1]
                    move(board, source[0], sourc[1], dest_x, dest_y)
                    
                    evaluation = evaluation_function(board)
                    
                    item_list[0] = board
                    item_list[1] = evaluation
                    
                    list.append(item_list)
        
        for i in range(0, len(list)):
            item = list[i]
            evaluation = item[1]
            
            if evaluation > 0:
                if evalutation > best_evaluation:
                    best_evaluation = evaluation
                    return item[0]
                    
                
                
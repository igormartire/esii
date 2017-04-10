#Função de movimentação no xadrez

board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
         ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
         ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]


def move (board, source_x, source_y, dest_x, dest_y):
    piece_source = board[dest_x][dest_y]
    piece_dest = board[source_x][source_y]
    board[source_x][source_y] = piece_source
    board[dest_x][dest_y] = piece_dest
    print (board)

move (board,7,4,5,5)


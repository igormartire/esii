# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Victor"
__date__ = "$30/04/2017 15:21:55$"
class Coordinate:
    def __init__(self, row, column):
        self.row = row
        self.column = column
	
    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def __repr__(self):
        return "(" + str(self.row) + ", " + str(self.column) + ")"

if __name__ == "__main__":


    def peao(piece, source):
        movimentos = []
	
        if (piece == 'p'):
            if (source.row < 7):
                source.row = source.row + 1
                movimentos.append(source)

        if (piece == 'P'):
            if (source.row > 0):
                source.row = source.row - 1
                movimentos.append(source)

        return movimentos


def torre(source):
    movimentos = []

    #gravando a posicao inicial da peca 
    x = source.row
    y = source.column
	
    for i in range(7):
        newSource = Coordinate(i, y)	
        movimentos.append(newSource) 	
	
    for i in range(7):
        newSource = Coordinate(x, i)	
        movimentos.append(newSource)
	
    #Percorrer lista de coordinate e eliminar a posicao atual da peca
    for i in range(14):
        if ((movimentos[i].row == x) & (movimentos[i].column == y)):
            movimentos.remove(movimentos [i])		
	
    return movimentos

def bispo(source):
    movimentos = []

    i = source.row 
    j = source.column

    #diagonal direita superior

    while ((i != 7) & (j != 7)):
        j = j + 1
        i = i + 1
        newSource = Coordinate(i, j) 
        movimentos.append(newSource)

    i = source.row 
    j = source.column
		
    #diagonal esquerda superior
    while ((i != 7) & (j != 0)):
        j = j-1
        i = i + 1
        newSource = Coordinate(i, j)
        movimentos.append(newSource)

    i = source.row 
    j = source.column

    #diagonal esquerda inferior

    while ((i != 0) & (j != 0)):
        j = j-1
        i = i-1
        newSource = Coordinate(i, j)
        movimentos.append(newSource)

    i = source.row 
    j = source.column

    #diagonal direita inferior
    while((i != 0) & (j != 7)):
        j = j + 1
        i = i-1
        newSource = Coordinate(i, j)
        movimentos.append(newSource)

    return movimentos

def cavalo(source):
    movimentos = []
    i = source.row 
    j = source.column

    #1 possibilidade 

    i = i + 2
    j = j + 1

    if((i <= 7) & (j <= 7)):
        newSource = Coordinate(i, j)
        movimentos.append(newSource)
	
    #2 possibilidade

    i = source.row 
    j = source.column

    i = i + 2
    j = j-1

    if ((i <= 7) & (j >= 0)):
        newSource = Coordinate(i, j)
        movimentos.append(newSource)

    #3 possibilidade 

    i = source.row 
    j = source.column

    i = i + 1
    j = j-2	

    if((i <= 7) & (j >= 0)):
        newSource = Coordinate(i, j)
        movimentos.append(newSource)

    #4 possibilidade

    i = source.row 
    j = source.column

    i = i-1
    j = j-2	

    if((i >= 0) & (j >= 0)):
        newSource = Coordinate(i, j)
        movimentos.append(newSource)

    #5 possibilidade

    i = source.row 
    j = source.column
	
    i = i + 1
    j = j + 2

    if((i <= 7) & (j <= 7)):
        newSource = Coordinate(i, j)
        movimentos.append(newSource)

    #6 possibilidade

    i = source.row 
    j = source.column
	
    i = i-1
    j = j + 2	
	
    if((i >= 0) & (j <= 7)):
        newSource = Coordinate(i, j)
        movimentos.append(newSource)
	
    #7 possibilidade

    i = source.row 
    j = source.column

    i = i-2
    j = j + 1	

    if((i >= 0) & (j <= 7)):
        newSource = Coordinate(i, j)
        movimentos.append(newSource)	

    #8 possibilidade
	
    i = source.row 
    j = source.column

    i = i-2
    j = j-1	

    if((i >= 0) & (j >= 0)):
        newSource = Coordinate(i, j)
        movimentos.append(newSource)		


    return movimentos

def rainha(source):

    movimentos = []

    #juncao dos movimentos da torre com os movimentos do bispo

    #gravando a posicao inicial da peca 
    x = source.row
    y = source.column
	
    for i in range(7):
        newSource = Coordinate(i, y)	
        movimentos.append(newSource) 	
	
    for i in range(7):
        newSource = Coordinate(x, i)	
        movimentos.append(newSource)
	
    #Percorrer lista de coordinate e eliminar os repetidos
    for i in range(12):
        if ((movimentos[i].row == x) & (movimentos[i].column == y)):
            movimentos.remove(movimentos [i])		
		
	
    #bispo

    i = source.row 
    j = source.column

    #diagonal direita superior

    while ((i != 7) & (j != 7)):
        j = j + 1
        i = i + 1
        newSource = Coordinate(i, j) 
        movimentos.append(newSource)

    i = source.row 
    j = source.column
		
    #diagonal esquerda superior
    while ((i != 7) & (j != 0)):
        j = j-1
        i = i + 1
        newSource = Coordinate(i, j)
        movimentos.append(newSource)

    i = source.row 
    j = source.column

    #diagonal esquerda inferior

    while ((i != 0) & (j != 0)):
        j = j-1
        i = i-1
        newSource = Coordinate(i, j)
        movimentos.append(newSource)

    i = source.row 
    j = source.column

    #diagonal direita inferior
    while((i != 0) & (j != 7)):
        j = j + 1
        i = i-1
        newSource = Coordinate(i, j)
        movimentos.append(newSource)

    return movimentos


def rei(source):
	
    movimentos = []

    i = source.row 
    j = source.column

    #1 possibilidade
    i = i + 1

    if (i <= 7):
        newSource = Coordinate(i, j)
        movimentos.append(newSource)

    #2 possibilidade

    i = source.row 
    j = source.column

    i = i-1

    if (i >= 0):
        newSource = Coordinate(i, j)
        movimentos.append(newSource)

    #3 possibilidade

    i = source.row 
    j = source.column

    j = j + 1	

    if(j <= 7):
        newSource = Coordinate(i, j)
        movimentos.append(newSource)

    #4 possibilidade
	
    i = source.row 
    j = source.column

    j = j-1

    if(j >= 0):
        newSource = Coordinate(i, j)
        movimentos.append(newSource)

    #5 possibilidade

    i = source.row 
    j = source.column

    i = i + 1
    j = j-1

    if((i <= 7) & (j >= 0)):
        newSource = Coordinate(i, j)
        movimentos.append(newSource)

    #6 possibilidade

    i = source.row 
    j = source.column

    i = i + 1
    j = j + 1

    if((i <= 7) & (j <= 7)):
        newSource = Coordinate(i, j)
        movimentos.append(newSource)

    #7 possibilidade

    i = source.row 
    j = source.column	

    i = i-1
    j = j + 1

    if((i >= 0) & (j <= 7)):
        newSource = Coordinate(i, j)
        movimentos.append(newSource)

    #8 possibilidade

    i = source.row 
    j = source.column	

    i = i-1
    j = j-1

    if((i >= 0) & (j >= 0)):
        newSource = Coordinate(i, j)
        movimentos.append(newSource)

    return movimentos

def minuscula(tabuleiro, movimentos):
    filtered_movements = []

    for i in movimentos:
        if not tabuleiro[i.row][i.column] in ['r', 'n', 'b', 'q', 'k', 'p']:
            filtered_movements.append(i)

    return filtered_movements

def maiuscula(tabuleiro, movimentos):
	
    filtered_movements = []

    for i in movimentos:
        if not tabuleiro[i.row][i.column] in ['R', 'N', 'B', 'Q', 'K', 'P']:
            filtered_movements.append(i)

    return filtered_movements

def destinations(piece, source, tabuleiro):
    movimentos = []
	
    if((piece == 'p') | (piece == 'P')):
        movimentos = peao(piece, source)

        if (piece == 'p'):
            movimentos = minuscula(tabuleiro, movimentos)
        else:
            movimentos = maiuscula(tabuleiro, movimentos)
		
    if((piece == 'r') | (piece == 'R')):
        movimentos = torre(source)

        if (piece == 'r'):
            movimentos = minuscula(tabuleiro, movimentos)
        else:
            movimentos = maiuscula(tabuleiro, movimentos)

    if((piece == 'n') | (piece == 'N')):
        movimentos = cavalo(source)

        if (piece == 'n'):
            movimentos = minuscula(tabuleiro, movimentos)
        else:
            movimentos = maiuscula(tabuleiro, movimentos)

    if((piece == 'b') | (piece == 'B')):
        movimentos = bispo(source)

        if (piece == 'b'):
            movimentos = minuscula(tabuleiro, movimentos)
        else:
            movimentos = maiuscula(tabuleiro, movimentos)

    if((piece == 'q') | (piece == 'Q')):
        movimentos = rainha(source)

        if (piece == 'q'):
            movimentos = minuscula(tabuleiro, movimentos)
        else:
            movimentos = maiuscula(tabuleiro, movimentos)

    if((piece == 'k') | (piece == 'K')):
        movimentos = rei(source)

        if (piece == 'k'):
            movimentos = minuscula(tabuleiro, movimentos)
        else:
            movimentos = maiuscula(tabuleiro, movimentos)

    return movimentos














def greedy(board, piece_player):
    list = []
    item_list = []
        
    evaluation = 0
    best_evaluation = 0
        
    new_destinations = []

    for i in range(0, 8):
        for j in range(0, 8):
            piece = board[i][j]
            source = Coordinate(i, j)    
            if piece_player == "M":
                if (piece == "r") | (piece == "n") | (piece == "b") | (piece == "q") | (piece == "k") | (piece == "p"):
                        
                    new_destinations = destinations(piece, source, board)

                    for k in range(0, len(new_destinations)):
                        dest = new_destinations[k]
                        dest_x = dest[0]
                        dest_y = dest[1]
                        move(board, source.row, source.column, dest_x, dest_y)

                        evaluation = evaluation_function(board)

                        item_list[0] = board
                        item_list[1] = evaluation

                        list.append(item_list)
            else:
                if (piece == "R") | (piece == "N") | (piece == "B") | (piece == "Q") | (piece == "K") | (piece == "P"):

                    new_destinations = destinations(piece, source, board)

                    for k in range(0, len(new_destinations)):
                        dest = new_destinations[k]
                        dest_x = dest[0]
                        dest_y = dest[1]
                        move(board, source.row, source.column, dest_x, dest_y)

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
 
board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

greedy(board, "M")

print (board)
                
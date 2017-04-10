WHITE = 0
BLACK = 1
GREEN = 2
RED = 3

def board_color(board, possible_destinations):
    colored_board = []
    next_color = BLACK
    for l in range(8):
        next_color = WHITE if next_color == BLACK else BLACK
        row = []
        for c in range(8):
            row.append(next_color)
            next_color = WHITE if next_color == BLACK else BLACK
        colored_board.append(row)
    
    for dst in possible_destinations:
        if board[dst['l']][dst['c']] != '.':
            colored_board[dst['l']][dst['c']] = RED
        else:
            colored_board[dst['l']][dst['c']] = GREEN

    return colored_board

board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

r = board_color(board, [{'l': 1,'c': 1}, {'l': 3,'c': 5}])

for row in r:
    print(row)
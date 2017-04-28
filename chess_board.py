#!/usr/bin/python
import pygame
import os
import copy
from pygame.locals import *
from enum import Enum


# TODO: move to commons (confirm)
SCREEN_TITLE = 'Chess'
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
BOARD_SIZE = 640
IMAGES_FOLDER_PATH = 'assets/images'

# TODO: comment this and color_board after integration (as docs)
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], # 8
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], # 7
    ['.', '.', '.', '.', '.', '.', '.', '.'], # 6
    ['.', '.', '.', '.', '.', '.', '.', '.'], # 5
    ['.', '.', '.', '.', '.', '.', '.', '.'], # 4
    ['.', '.', '.', '.', '.', '.', '.', '.'], # 3
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], # 2
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'], # 1
    # a    b    c    d    e    f    g    h
]
color_board = [
    [1, 2, 1, 0, 1, 0, 1, 0], # 8
    [0, 1, 0, 1, 0, 1, 0, 1], # 7
    [1, 3, 1, 0, 1, 0, 1, 0], # 6
    [0, 1, 0, 1, 0, 1, 0, 1], # 5
    [1, 0, 1, 0, 1, 0, 1, 0], # 4
    [0, 1, 0, 1, 0, 1, 0, 1], # 3
    [1, 0, 1, 0, 1, 0, 1, 0], # 2
    [0, 1, 0, 1, 0, 1, 0, 1], # 1
    #a  b  c  d  e  f  g  h
]


class Color(Enum):
    BLACK = (100, 100, 100)
    WHITE = (230, 230, 230)
    GREEN = (50, 200, 50)
    RED = (200, 50, 50)

    def get_rgb(code):
        if code == 0:
            return Color.BLACK.value
        if code == 1:
            return Color.WHITE.value
        if code == 2:
            return Color.GREEN.value
        if code == 3:
            return  Color.RED.value


def load_png(file_name):
    """ Load image and return image object"""
    """ 
        Não precisa se preocupar com essa função, ela é só uma função auxiliar para garantir que
        as imagens sejam carregadas no formato certo
    """
    fullname = os.path.join(IMAGES_FOLDER_PATH, file_name + '.png')
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except (pygame.error):
        print('Error loading image', fullname)
        raise(pygame.error('a'))
    return image


class ChessPiece(pygame.sprite.Sprite):
    """"
    Não precisa se preocupar muito com essa classe também, é apenas uma 'imagem'
    """
    def __init__(self, name, image_surface, rect):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = image_surface
        self.rect = pygame.Rect(rect)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

    def was_clicked(self, click_position):
        return self.rect.collidepoint(click_position)


def create_chess_piece(piece_code, cell_size, cell_rect):
    """
    Uma factory de peças simplesmente
    :returns ChessPiece
    """
    piece_image = None
    if piece_code == 'P':
        piece_image = WHITE_PAWN_IMAGE
        name = 'white pawn'
    elif piece_code == 'R':
        piece_image = WHITE_ROOK_IMAGE
        name = 'white rook'
    elif piece_code == 'N':
        piece_image = WHITE_KNIGHT_IMAGE
        name = 'white knight'
    elif piece_code == 'B':
        piece_image = WHITE_BISHOP_IMAGE
        name = 'white bishop'
    elif piece_code == 'Q':
        piece_image = WHITE_QUEEN_IMAGE
        name = 'white queen'
    elif piece_code == 'K':
        piece_image = WHITE_KING_IMAGE
        name = 'white king'
    elif piece_code == 'p':
        piece_image = BLACK_PAWN_IMAGE
        name = 'black pawn'
    elif piece_code == 'r':
        piece_image = BLACK_ROOK_IMAGE
        name = 'black rook'
    elif piece_code == 'n':
        piece_image = BLACK_KNIGHT_IMAGE
        name = 'black knight'
    elif piece_code == 'b':
        piece_image = BLACK_BISHOP_IMAGE
        name = 'black bishop'
    elif piece_code == 'q':
        piece_image = BLACK_QUEEN_IMAGE
        name = 'black queen'
    elif piece_code == 'k':
        piece_image = BLACK_KING_IMAGE
        name = 'black king'

    chess_piece = None
    if piece_image is not None:
        chess_piece_image = pygame.transform.scale(
            piece_image, (int(cell_size), int(cell_size)))
        chess_piece = ChessPiece(name, chess_piece_image, cell_rect)

    return chess_piece


def setup_board(board, color_board):
    """
    Recebe um board e um color_board (ambos são matrizes)
    A partir deles, monta um tabuleiro com as respectivas peças e cores de cada célula
    """
    # Surface é a classe que representa uma imagem, basicamente, a qual pode ser pintada na tela
    board_surface = pygame.Surface((BOARD_SIZE, BOARD_SIZE)).convert()
    chess_pieces = []
    num_of_cells = len(board)
    cell_size = BOARD_SIZE / num_of_cells
    for row in range(num_of_cells):
        for col in range(num_of_cells):
            cell_rect = (col * cell_size, row * cell_size, cell_size, cell_size)
            cell_color = Color.get_rgb(color_board[row][col])
            board_surface.fill(cell_color, cell_rect)
            cell_code = board[row][col]
            chess_piece = create_chess_piece(cell_code, cell_size, cell_rect)
            if chess_piece is not None:
                chess_pieces.append(chess_piece)

    return board_surface, chess_pieces

def get_cell_by_position(position, board):
    """
    Pega a posição de uma célula dentro do board (0..7)x(0..7)
    de acordo com a position
    """
    num_of_cells = len(board)
    cell_size = BOARD_SIZE / num_of_cells
    for row in range(num_of_cells):
        for col in range(num_of_cells):
            cell = (col * cell_size, row * cell_size, cell_size, cell_size)
            cell_rect = pygame.Rect(cell)
            if cell_rect.collidepoint(position):
                return (row, col)


if __name__ == '__main__':
    # Initialise screen
    # Necessário para "rodar" o joguinho
    pygame.init()
    # A janela do jogo em si, com tamanho WIDTHxHEIGHT (lá em cima setados)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Título da janela
    pygame.display.set_caption(SCREEN_TITLE)

    # Load sprites
    # Ainda vou pensar em como tirar isso daqui e carregar em outro lugar hehe
    WHITE_PAWN_IMAGE = load_png('chess-pieces/white-pawn')
    WHITE_BISHOP_IMAGE = load_png('chess-pieces/white-bishop')
    WHITE_KING_IMAGE = load_png('chess-pieces/white-king')
    WHITE_KNIGHT_IMAGE = load_png('chess-pieces/white-knight')
    WHITE_QUEEN_IMAGE = load_png('chess-pieces/white-queen')
    WHITE_ROOK_IMAGE = load_png('chess-pieces/white-rook')
    BLACK_PAWN_IMAGE = load_png('chess-pieces/black-pawn')
    BLACK_BISHOP_IMAGE = load_png('chess-pieces/black-bishop')
    BLACK_KING_IMAGE = load_png('chess-pieces/black-king')
    BLACK_KNIGHT_IMAGE = load_png('chess-pieces/black-knight')
    BLACK_QUEEN_IMAGE = load_png('chess-pieces/black-queen')
    BLACK_ROOK_IMAGE = load_png('chess-pieces/black-rook')

    # Events loop
    running = True
    # Posição da última peça clicada
    last_held_piece_pos = None

    while running:
        # Pinta a tela de preto
        screen.fill((0,0,0))
        # Pega posição (x,y) do mouse
        mouse_position = pygame.mouse.get_pos()
        # Pega a posição das células (a partir da posição do mouse)
        cell_x, cell_y = get_cell_by_position(mouse_position, board)
        # Para cada evento que ocorreu (cliques, teclas, etc.)
        for event in pygame.event.get():
            # Se clicou para fechar a janela
            if event.type == QUIT:
                running = False
###### Início da lógica de movimentação #######
            # Se apartou algum botão do mouse (ainda vou adicionar restrição para apenas o botão esquerdo)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # If wasn't holding a piece before AND clicked on a piece (that is, board value != '.')
                if last_held_piece_pos is None \
                        and board[cell_x][cell_y] != '.':
                    # Hold the piece
                    last_held_piece_pos = cell_x, cell_y
                    print("Clicked on cell: {} which contains a {}".format(
                        last_held_piece_pos, board[cell_x][cell_y]))
            # Se soltou algum botão do mouse E estava segurando alguma peça
            elif event.type == pygame.MOUSEBUTTONUP \
                    and last_held_piece_pos is not None:
                # Substitui o valor do board na célula destino pelo valor da célula de origem
                # Pega a posição de origem (para fazer swap)
                origin_piece_x = last_held_piece_pos[0]
                origin_piece_y = last_held_piece_pos[1]
                # Pega o valor da posição de origem (letra da peça)
                origin_piece = board[origin_piece_x][origin_piece_y]
                # Remove peça de origem do tabuleiro (substitui por '.')
                board[origin_piece_x][origin_piece_y] = '.'
                # Substitui peça na célula de destino
                board[cell_x][cell_y] = origin_piece
                # "solta" a peça
                last_held_piece_pos = None
##### Fim da lógica de movimentação ######

        # give it a margin if board is smaller than screen
        # somente por estética, pode ignorar
        board_position = (
            (SCREEN_WIDTH - BOARD_SIZE) / 2,
            (SCREEN_HEIGHT - BOARD_SIZE) / 2,
        )

        # Pega nova surface atualizada pelas linhas acima
        board_surface, chess_pieces = setup_board(board, color_board)
        # Blitting => drawing updates to the screen
        # pinta o tabuleiro
        screen.blit(board_surface, board_position)
        # pinta cada peça em sua respectiva nova posição
        for chess_piece in chess_pieces:
            screen.blit(chess_piece.image, chess_piece.rect)

        # updating everything (necessary)
        pygame.display.update()

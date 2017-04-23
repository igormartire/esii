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
    def __init__(self, name, image_surface, rect):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = image_surface
        self.rect = rect
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

def create_chess_piece(piece_code, cell_size, cell_rect):
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

def draw_board(board, color_board):
    # TODO: comment this after integration (as docs)
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
                #board_surface.blit(chess_piece.image, chess_piece.rect)

    return board_surface, chess_pieces

if __name__ == '__main__':
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(SCREEN_TITLE)

    # Load sprites
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

    # Fill background
    background = pygame.Surface(screen.get_size())
    # Convert the Surface to the pixel format (necessary for all Surfaces)
    background = background.convert()
    background.fill(Color.WHITE.value)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Events loop
    running = True
    holding_piece = False
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                downclick_pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONUP:
                print("mouse up")

        board_surface, chess_pieces = draw_board(['test_board'], ['test_board_color'])
        # give it a margin if board is smaller than screen
        board_position = (
            (SCREEN_WIDTH - BOARD_SIZE) / 2,
            (SCREEN_HEIGHT - BOARD_SIZE) / 2,
        )


        # Blitting
        screen.blit(background, (0, 0))
        screen.blit(board_surface, board_position)
        for chess_piece in chess_pieces:
            screen.blit(chess_piece.image, chess_piece.rect)
        pygame.display.flip()

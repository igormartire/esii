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
    def __init__(self, image_file, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_png(image_file)
        self.rect = rect
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()


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
    num_of_cells = len(board)
    cell_size = BOARD_SIZE / num_of_cells
    for row in range(num_of_cells):
        for col in range(num_of_cells):
            cell_rect = (col * cell_size, row * cell_size, cell_size, cell_size)
            cell_color = Color.get_rgb(color_board[row][col])
            board_surface.fill(cell_color, cell_rect)

            # Check which image we shall blit on board_surface
            piece_image = None
            if board[row][col] == 'P':
                piece_image = WHITE_PAWN_IMAGE
            elif board[row][col] == 'R':
                piece_image = WHITE_ROOK_IMAGE
            elif board[row][col] == 'N':
                piece_image = WHITE_KNIGHT_IMAGE
            elif board[row][col] == 'B':
                piece_image = WHITE_BISHOP_IMAGE
            elif board[row][col] == 'Q':
                piece_image = WHITE_QUEEN_IMAGE
            elif board[row][col] == 'K':
                piece_image = WHITE_KING_IMAGE
            elif board[row][col] == 'p':
                piece_image = BLACK_PAWN_IMAGE
            elif board[row][col] == 'r':
                piece_image = BLACK_ROOK_IMAGE
            elif board[row][col] == 'n':
                piece_image = BLACK_KNIGHT_IMAGE
            elif board[row][col] == 'b':
                piece_image = BLACK_BISHOP_IMAGE
            elif board[row][col] == 'q':
                piece_image = BLACK_QUEEN_IMAGE
            elif board[row][col] == 'k':
                piece_image = BLACK_KING_IMAGE

            if piece_image is not None:
                chess_piece = pygame.transform.scale(piece_image, (int(cell_size), int(cell_size)))
                board_surface.blit(chess_piece, cell_rect)

    return board_surface

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

    # Event loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        screen.blit(background, (0, 0))
        # give it a margin if board is smaller than screen
        board_position = (
            (SCREEN_WIDTH - BOARD_SIZE) / 2,
            (SCREEN_HEIGHT - BOARD_SIZE) / 2,
        )
        screen.blit(draw_board(['test_board'], ['test_board_color']), board_position)
        pygame.display.flip()

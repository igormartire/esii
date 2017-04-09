#!/usr/bin/python
import pygame
from pygame.locals import *
from enum import Enum


# TODO: move to commons (confirm)
SCREEN_TITLE = 'Chess'
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
BOARD_SIZE = 640
IMAGES_FOLDER_PATH = 'images'


class Color(Enum):
    BLACK = (50, 50, 50)
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


class ChessPiece(pygame.sprite.Sprite):
    def __init__(self, code):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png(get_name_from_code(code) + '.png')
        self.area = pygame.display.get_surface().get_rect()

    def get_name_from_code(code):
        if code == 'p':
            return 'black-pawn'
        elif code =='P':
            return 'white-pawn'
        else:
            return 'white-queen'


def load_png(file_name):
    """ Load image and return image object"""
    fullname = os.path.join('images', file_name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except (pygame.error, message):
        print('Cannot load image:', fullname)
        raise(SystemExit, message)
    return image, image.get_rect()

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

    return board_surface

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(SCREEN_TITLE)

    # Fill background
    background = pygame.Surface(screen.get_size())
    # Convert the Surface to the pixel format (necessary for all Surfaces)
    background = background.convert()
    background.fill(Color.WHITE.value)

    # Display some text
    '''
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)
    '''

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        # give it a margin if board is smaller than screen
        board_position = (
            (SCREEN_WIDTH - BOARD_SIZE) / 2,
            (SCREEN_HEIGHT - BOARD_SIZE) / 2,
        )
        screen.blit(draw_board(['test_board'], ['test_board_color']), board_position)
        pygame.display.flip()


if __name__ == '__main__':
    main()

pygame.init()

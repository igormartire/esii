#!/usr/bin/python
import pygame
from pygame.locals import *


# TODO: move to commons (confirm)
SCREEN_TITLE = 'Chess'
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
BOARD_SIZE = 640
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GREEN_COLOR = (0, 255, 0)
RED_COLOR = (255, 0, 0)
IMAGES_FOLDER_PATH = 'images'


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

def draw_board(board):
    # TODO: remove this after integration
    board = [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], # 1
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], # 2
        ['.', '.', '.', '.', '.', '.', '.', '.'], # 3
        ['.', '.', '.', '.', '.', '.', '.', '.'], # 4
        ['.', '.', '.', '.', '.', '.', '.', '.'], # 5
        ['.', '.', '.', '.', '.', '.', '.', '.'], # 6
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], # 7
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'], # 8
    ]

    board_surface = pygame.Surface((BOARD_SIZE, BOARD_SIZE)).convert()
    num_of_cells = len(board)
    cell_size = BOARD_SIZE / num_of_cells
    colors = [WHITE_COLOR, BLACK_COLOR]
    for row in range(num_of_cells):
        color_index = row % 2  # Change starting color on each row
        for col in range(num_of_cells):
            board_cell = (col * cell_size, row * cell_size, cell_size, cell_size)
            board_surface.fill(colors[color_index], board_cell)
            # flip color
            color_index = (color_index + 1) % 2

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
    background.fill((250, 250, 250))

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
        screen.blit(draw_board(['remove']), board_position)
        pygame.display.flip()


if __name__ == '__main__':
    main()

pygame.init()

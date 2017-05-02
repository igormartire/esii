#!/usr/bin/python
import pygame
import os

from pygame.locals import *

from chess.core.models import Coordinate, Color, Piece
from chess.core.utils import INITIAL_BOARD, TEST_COLORED_BOARD

# TODO: move to commons (confirm)
SCREEN_TITLE = 'Chess'
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
BOARD_SIZE = 640
IMAGES_FOLDER_PATH = 'assets/images'


colored_board = TEST_COLORED_BOARD


def load_png(file_name):
    """ Load image and return image object"""
    fullname = os.path.join(IMAGES_FOLDER_PATH, file_name + '.png')
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error:
        print('Error loading image', fullname)
        raise(pygame.error('a'))
    return image


class ChessPiece(pygame.sprite.Sprite):
    def __init__(self, name, image_surface, rect):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = image_surface
        self.rect = pygame.Rect(rect)
        self.screen = pygame.display.get_surface()
        self.area = screen.get_rect()

    def was_clicked(self, click_position):
        return self.rect.collidepoint(click_position)


def create_chess_piece(piece, cell_size, cell_rect):
    piece_image = None
    if piece == Piece.WHITE_PAWN:
        piece_image = WHITE_PAWN_IMAGE
        name = 'white pawn'
    elif piece == Piece.WHITE_ROOK:
        piece_image = WHITE_ROOK_IMAGE
        name = 'white rook'
    elif piece == Piece.WHITE_KNIGHT:
        piece_image = WHITE_KNIGHT_IMAGE
        name = 'white knight'
    elif piece == Piece.WHITE_BISHOP:
        piece_image = WHITE_BISHOP_IMAGE
        name = 'white bishop'
    elif piece == Piece.WHITE_QUEEN:
        piece_image = WHITE_QUEEN_IMAGE
        name = 'white queen'
    elif piece == Piece.WHITE_KING:
        piece_image = WHITE_KING_IMAGE
        name = 'white king'
    elif piece == Piece.BLACK_PAWN:
        piece_image = BLACK_PAWN_IMAGE
        name = 'black pawn'
    elif piece == Piece.BLACK_ROOK:
        piece_image = BLACK_ROOK_IMAGE
        name = 'black rook'
    elif piece == Piece.BLACK_KNIGHT:
        piece_image = BLACK_KNIGHT_IMAGE
        name = 'black knight'
    elif piece == Piece.BLACK_BISHOP:
        piece_image = BLACK_BISHOP_IMAGE
        name = 'black bishop'
    elif piece == Piece.BLACK_QUEEN:
        piece_image = BLACK_QUEEN_IMAGE
        name = 'black queen'
    elif piece == Piece.BLACK_KING:
        piece_image = BLACK_KING_IMAGE
        name = 'black king'

    chess_piece = None
    if piece_image is not None:
        chess_piece_image = pygame.transform.scale(
            piece_image, (int(cell_size), int(cell_size)))
        chess_piece = ChessPiece(name, chess_piece_image, cell_rect)

    return chess_piece


def setup_board(board, color_board):
    board_surface = pygame.Surface((BOARD_SIZE, BOARD_SIZE)).convert()
    chess_pieces = []
    num_of_cells = len(board)
    cell_size = BOARD_SIZE / num_of_cells
    for row in range(num_of_cells):
        for col in range(num_of_cells):
            cell_rect = (col * cell_size, row * cell_size, cell_size, cell_size)
            cell_color = Color.get_rgb(color_board[row][col])
            board_surface.fill(cell_color, cell_rect)
            cell_value = board[row][col]
            chess_piece = create_chess_piece(cell_value, cell_size, cell_rect)
            if chess_piece is not None:
                chess_pieces.append(chess_piece)

    return board_surface, chess_pieces


def get_cell_by_position(position, board):
    num_of_cells = len(board)
    cell_size = BOARD_SIZE / num_of_cells
    for row in range(num_of_cells):
        for col in range(num_of_cells):
            cell = (col * cell_size, row * cell_size, cell_size, cell_size)
            cell_rect = pygame.Rect(cell)
            if cell_rect.collidepoint(position):
                return row, col


# give it a margin if board is smaller than screen
def board_position():
    return (SCREEN_WIDTH - BOARD_SIZE) / 2, (SCREEN_HEIGHT - BOARD_SIZE) / 2


def can_move_piece(clicked_piece, last_held_piece):
    if last_held_piece is None and clicked_piece != Piece.NONE:
        return True
    return False


if __name__ == '__main__':
    chess_board = INITIAL_BOARD
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

    # Game Loop
    running = True
    last_held_piece_pos = None
    while running:
        mouse_position = pygame.mouse.get_pos()
        cell_x, cell_y = get_cell_by_position(mouse_position, chess_board)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clicked_piece = chess_board[cell_x][cell_y]
                if can_move_piece(clicked_piece, last_held_piece_pos):
                    last_held_piece_pos = cell_x, cell_y
                    print("Clicked on cell: {} which contains a {}".format(
                        last_held_piece_pos, clicked_piece))
            elif event.type == pygame.MOUSEBUTTONUP \
                    and last_held_piece_pos is not None:
                origin_piece_x = last_held_piece_pos[0]
                origin_piece_y = last_held_piece_pos[1]
                origin_piece = chess_board[origin_piece_x][origin_piece_y]
                chess_board[origin_piece_x][origin_piece_y] = Piece.NONE
                chess_board[cell_x][cell_y] = origin_piece
                last_held_piece_pos = None

        board_surface, chess_pieces = setup_board(chess_board, colored_board)
        screen.blit(board_surface, board_position())
        for chess_piece in chess_pieces:
            screen.blit(chess_piece.image, chess_piece.rect)

        pygame.display.update()

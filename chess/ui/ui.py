import os
import copy

import pygame
from pygame.locals import *

from chess.core.models import Coordinate, Color, Piece
from chess.core.utils import initial_board, BLACK_PIECES, WHITE_PIECES
from chess.core.possible_destinations import destinations
from chess.core.coloring import color_board
from chess.core.moving import move
from chess.ai.score import score_board

SCREEN_TITLE = 'Chess'
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
BOARD_SIZE = 640
IMAGES_FOLDER_PATH = 'chess/ui/assets/images'


class UI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(SCREEN_TITLE)
        self.sprites = {
            "WHITE_PAWN_IMAGE": self.load_png('chess-pieces/white-pawn'),
            "WHITE_BISHOP_IMAGE": self.load_png('chess-pieces/white-bishop'),
            "WHITE_KING_IMAGE": self.load_png('chess-pieces/white-king'),
            "WHITE_KNIGHT_IMAGE": self.load_png('chess-pieces/white-knight'),
            "WHITE_QUEEN_IMAGE": self.load_png('chess-pieces/white-queen'),
            "WHITE_ROOK_IMAGE": self.load_png('chess-pieces/white-rook'),
            "BLACK_PAWN_IMAGE": self.load_png('chess-pieces/black-pawn'),
            "BLACK_BISHOP_IMAGE": self.load_png('chess-pieces/black-bishop'),
            "BLACK_KING_IMAGE": self.load_png('chess-pieces/black-king'),
            "BLACK_KNIGHT_IMAGE": self.load_png('chess-pieces/black-knight'),
            "BLACK_QUEEN_IMAGE": self.load_png('chess-pieces/black-queen'),
            "BLACK_ROOK_IMAGE": self.load_png('chess-pieces/black-rook')
        }

    def refresh(self, chess_board, colored_board):
        board_surface, chess_pieces = self.setup_board(chess_board, colored_board)
        self.screen.blit(board_surface, board_position())
        for chess_piece in chess_pieces:
            self.screen.blit(chess_piece.image, chess_piece.rect)
        pygame.display.update()

    def create_chess_piece(self, piece, cell_size, cell_rect):
        if (piece == Piece.NONE):
            piece_image = None
        else:
            piece_image = self.sprites[piece.name + '_IMAGE']

        chess_piece = None
        if piece_image is not None:
            chess_piece_image = pygame.transform.scale(
                piece_image, (int(cell_size), int(cell_size)))
            chess_piece = ChessPiece(chess_piece_image, cell_rect)

        return chess_piece

    def setup_board(self, board, color_board):
        board_surface = pygame.Surface((BOARD_SIZE, BOARD_SIZE)).convert()
        chess_pieces = []
        num_of_cells = len(board)
        cell_size = BOARD_SIZE / num_of_cells
        for row in range(num_of_cells):
            for col in range(num_of_cells):
                cell_rect = (col * cell_size, row * cell_size, cell_size, cell_size)
                cell_color_rgb = color_board[row][col].rgb
                print(cell_color_rgb)
                board_surface.fill(cell_color_rgb, cell_rect)
                cell_value = board[row][col]
                chess_piece = self.create_chess_piece(cell_value, cell_size, cell_rect)
                if chess_piece is not None:
                    chess_pieces.append(chess_piece)

        return board_surface, chess_pieces

    def load_png(self, file_name):
        """ Load image and return image object"""
        fullname = os.path.join(IMAGES_FOLDER_PATH, file_name + '.png')
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        return image


class ChessPiece(pygame.sprite.Sprite):
    def __init__(self, image_surface, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_surface
        self.rect = pygame.Rect(rect)

    def was_clicked(self, click_position):
        return self.rect.collidepoint(click_position)


def get_coordinates_by_position(position, board):
    num_of_cells = len(board)
    cell_size = BOARD_SIZE / num_of_cells
    for row in range(num_of_cells):
        for col in range(num_of_cells):
            cell = (col * cell_size, row * cell_size, cell_size, cell_size)
            cell_rect = pygame.Rect(cell)
            if cell_rect.collidepoint(position):
                return Coordinate(row, col)


def board_position():
    return (SCREEN_WIDTH - BOARD_SIZE) / 2, (SCREEN_HEIGHT - BOARD_SIZE) / 2


def is_holding_piece(piece_coord):
    return piece_coord is not None


def can_move_piece(clicked_piece, held_piece_coord):
    if not is_holding_piece(held_piece_coord) and clicked_piece != Piece.NONE \
            and clicked_piece in WHITE_PIECES:
        return True
    return False


def greedy_move(board):
    best_move = None
    best_value = -9999
    for row in range(8):
        for column in range(8):
            piece = board[row][column]
            if piece in BLACK_PIECES:
                src = Coordinate(row, column)
                dests = destinations(board, src)
                for dest in dests:
                    possible_board = move(board, src, dest)
                    possible_value = score_board(possible_board)
                    if possible_value > best_value:
                        best_value = possible_value
                        best_move = (src, dest)
    return best_move


def random_movement(board):
    for row in range(8):
        for column in range(8):
            piece = board[row][column]
            if piece in BLACK_PIECES:
                src = Coordinate(row, column)
                dests = destinations(board, src)
                if (dests):
                    return (src, dests[0])


def run():
    ui = UI()
    chess_board = initial_board()

# region game loop
    running = True
    held_piece_coord = None
    player_turn = True
    print("Player turn...")
    while running:
        mouse_position = pygame.mouse.get_pos()
        cell_coord = get_coordinates_by_position(
            mouse_position, chess_board)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif player_turn and event.type == pygame.MOUSEBUTTONDOWN:
                clicked_piece = chess_board[cell_coord.row][cell_coord.column]
                if can_move_piece(clicked_piece, held_piece_coord):
                    held_piece_coord = Coordinate(
                        cell_coord.row, cell_coord.column)
                    print("Clicked on cell: {} which contains a {}".format(
                        held_piece_coord, clicked_piece))
            elif player_turn and event.type == pygame.MOUSEBUTTONUP:
                if is_holding_piece(held_piece_coord):
                    possible_destinations = destinations(
                        chess_board, held_piece_coord)
                    if cell_coord in possible_destinations:
                        chess_board = move(
                            chess_board, held_piece_coord, cell_coord)
                        player_turn = False
                        print("Player moved!")
                        print("Computer turn...")
                    else:
                        print("You cannot do that!")
                        print("Player turn still...")
                    held_piece_coord = None

        possible_destinations = []
        if player_turn and is_holding_piece(held_piece_coord):
            piece = chess_board[held_piece_coord.row][held_piece_coord.column]
            possible_destinations = destinations(chess_board, held_piece_coord)

        colored_board = color_board(chess_board, possible_destinations)

        if not player_turn:
            movement = greedy_move(chess_board)
            #movement = random_movement(chess_board)
            chess_board = move(chess_board, movement[0], movement[1])
            print("Computer moved!")
            player_turn = True
            print("Player turn...")

        ui.refresh(chess_board, colored_board)
# endregion game loop

    pygame.quit()


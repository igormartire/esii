import os
import copy
import time
from functools import partial

import pygame
from pygame.locals import *

import chess.core.utils
from chess.core.models import Coordinate, Color, Piece, Player
from chess.core.utils import initial_board, BLACK_PIECES, WHITE_PIECES
from chess.core.query import (destinations,
                              is_check_for_player,
                              is_checkmate_for_player,
                              is_stalemate_for_player,
                              is_impossible_checkmate)
from chess.core.coloring import color_board
from chess.core.moving import move
from chess.ai.score import score_board
from chess.ai.greedy import greedy_move
from chess.core.game import Game

SCREEN_TITLE = 'Chess'
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 740
BOARD_SIZE = 640
CELL_BORDER = 3
IMAGES_FOLDER_PATH = 'chess/ui/assets/images'


class UI:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont("monospace", 50)
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
        self.assets = {
            'title': self.load_png('title'),
            'logo_small': self.load_png('logo_small'),
            'bg': self.load_png('bg'),
        }

        self.__displayed_text = self.font.render("", 1, (255, 255, 255))

        self.game_difficulty = 0

    def display_text(self, text, color=(255, 255, 255)):
        self.__displayed_text = self.font.render(text, 1, color)

    def animate(self, board, move_diff):
        B = Color.BLACK
        W = Color.WHITE
        colored_board = [[W, B, W, B, W, B, W, B],
                         [B, W, B, W, B, W, B, W],
                         [W, B, W, B, W, B, W, B],
                         [B, W, B, W, B, W, B, W],
                         [W, B, W, B, W, B, W, B],
                         [B, W, B, W, B, W, B, W],
                         [W, B, W, B, W, B, W, B],
                         [B, W, B, W, B, W, B, W]]
        dH = move_diff[1].row - move_diff[0].row
        dL = move_diff[1].column - move_diff[0].column
        for i in range(10):
            t = i / 10.0
            self.screen.fill((0, 0, 0))
            board_surface = pygame.Surface((BOARD_SIZE, BOARD_SIZE)).convert()
            chess_pieces = []
            num_of_cells = len(board)
            cell_size = (BOARD_SIZE / num_of_cells)
            for row in range(num_of_cells):
                for col in range(num_of_cells):
                    cell_rect = (col * cell_size, row * cell_size,
                                 cell_size - CELL_BORDER,
                                 cell_size - CELL_BORDER)
                    if row == move_diff[1].row and col == move_diff[1].column:
                        piece_cell_rect = (
                            (move_diff[0].column + t * dL) * cell_size +
                            board_position()[0],
                            (move_diff[0].row + t * dH) * cell_size +
                            board_position()[1],
                            cell_size - CELL_BORDER, cell_size - CELL_BORDER)
                    else:
                        piece_cell_rect = (
                            col * cell_size + board_position()[0],
                            row * cell_size + board_position()[1],
                            cell_size - CELL_BORDER,
                            cell_size - CELL_BORDER)
                    cell_color_rgb = colored_board[row][col].rgb
                    board_surface.fill(cell_color_rgb, cell_rect)
                    cell_value = board[row][col]
                    chess_piece = self.create_chess_piece(
                        cell_value, cell_size, piece_cell_rect)
                    if chess_piece is not None:
                        chess_pieces.append(chess_piece)

            self.screen.blit(board_surface, board_position())
            for chess_piece in chess_pieces:
                self.screen.blit(chess_piece.image, chess_piece.rect)
            text_rect = self.__displayed_text.get_rect(
                center=(SCREEN_WIDTH / 2, 50))
            self.screen.blit(self.__displayed_text, text_rect)
            pygame.display.update()
            time.sleep(0.03)

    def refresh(self, chess_board, colored_board):
        self.screen.fill((0, 0, 0))

        board_surface, chess_pieces = self.setup_board(
            chess_board, colored_board)
        self.screen.blit(board_surface, board_position())
        for chess_piece in chess_pieces:
            self.screen.blit(chess_piece.image, chess_piece.rect)

        text_rect = self.__displayed_text.get_rect(
            center=(SCREEN_WIDTH / 2, 50))
        self.screen.blit(self.__displayed_text, text_rect)

        pygame.display.update()

    def create_chess_piece(self, piece, cell_size, cell_rect):
        if piece == Piece.NONE:
            piece_image = None
        else:
            piece_image = self.sprites[piece.name + '_IMAGE']

        chess_piece = None
        if piece_image is not None:
            chess_piece_image = pygame.transform.scale(
                piece_image, (int(cell_size), int(cell_size)))
            chess_piece = ChessPiece(chess_piece_image, cell_rect, piece)

        return chess_piece

    def setup_board(self, board, color_board):
        board_surface = pygame.Surface((BOARD_SIZE, BOARD_SIZE)).convert()
        chess_pieces = []
        num_of_cells = len(board)
        cell_size = (BOARD_SIZE / num_of_cells)
        for row in range(num_of_cells):
            for col in range(num_of_cells):
                cell_rect = (
                    col * cell_size,
                    row * cell_size,
                    cell_size - CELL_BORDER,
                    cell_size - CELL_BORDER)
                cell_color_rgb = color_board[row][col].rgb
                board_surface.fill(cell_color_rgb, cell_rect)
                cell_value = board[row][col]

                piece_rect = (
                    col * cell_size + board_position()[0],
                    row * cell_size + board_position()[1],
                    cell_size - CELL_BORDER,
                    cell_size - CELL_BORDER)

                chess_piece = self.create_chess_piece(
                    cell_value, cell_size, piece_rect)
                if chess_piece is not None:
                    chess_pieces.append(chess_piece)

        return board_surface, chess_pieces

    def load_png(self, file_name):
        fullname = os.path.join(IMAGES_FOLDER_PATH, file_name + '.png')
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        return image


class ChessPiece(pygame.sprite.Sprite):
    def __init__(self, image_surface, rect, symbol=''):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_surface
        self.rect = pygame.Rect(rect)
        self.symbol = symbol

    def was_clicked(self, click_position):
        return self.rect.collidepoint(click_position)

    def __str__(self):
        return self.symbol


def get_coordinates_by_position(position, board):
    num_of_cells = len(board)
    cell_size = BOARD_SIZE / num_of_cells
    for row in range(num_of_cells):
        for col in range(num_of_cells):
            cell = (col * cell_size + board_position()[0],
                    row * cell_size + board_position()[1],
                    cell_size, cell_size)
            cell_rect = pygame.Rect(cell)
            if cell_rect.collidepoint(position):
                return Coordinate(row, col)


def get_rect_by_coordinates(coordinates, board):
    num_of_cells = len(board)
    cell_size = BOARD_SIZE / num_of_cells
    board_x, board_y = board_position()
    rect = pygame.Rect(board_x + coordinates.column * cell_size,
                       board_y + coordinates.row * cell_size,
                       BOARD_SIZE / 8, BOARD_SIZE / 8)

    return rect


def board_position():
    return (
        (SCREEN_WIDTH - BOARD_SIZE) / 2,
        (SCREEN_HEIGHT - BOARD_SIZE) / 2 + 50)


def is_holding_piece(piece_coord):
    return piece_coord is not None


def can_move_piece(clicked_piece, held_piece_coord):
    if not is_holding_piece(held_piece_coord) and clicked_piece != Piece.NONE \
            and clicked_piece in WHITE_PIECES:
        return True
    return False


def promotion_callback_factory(ui):
    def promotion_callback(board):
        ui.refresh(board, color_board(board, []))

        black = pygame.color.Color('Black')
        green = pygame.color.Color('Green')
        red = pygame.color.Color('Red')

        top_notification_surface = pygame.Surface((BOARD_SIZE, 100)).convert()
        top_notification_surface.fill(black, (0, 0, BOARD_SIZE, 100))
        promotion_text = ui.font.render("Promote: ", 1, green)
        text_rect = promotion_text.get_rect()
        text_rect.centery = top_notification_surface.get_rect().centery
        text_rect.left = 50
        top_notification_surface.blit(promotion_text, text_rect)
        ui.screen.blit(top_notification_surface, (0, 0))

        initialx = text_rect.right + 50
        y = 10
        size = 80
        space = 11

        pieces_rects = [
            (initialx + ((size + space) * 0), y, size, size),
            (initialx + ((size + space) * 1), y, size, size),
            (initialx + ((size + space) * 2), y, size, size),
            (initialx + ((size + space) * 3), y, size, size)
        ]

        selected_piece = None

        chess_pieces = [
            ui.create_chess_piece(Piece.WHITE_QUEEN, size, pieces_rects[0]),
            ui.create_chess_piece(Piece.WHITE_ROOK, size, pieces_rects[1]),
            ui.create_chess_piece(Piece.WHITE_KNIGHT, size, pieces_rects[2]),
            ui.create_chess_piece(Piece.WHITE_BISHOP, size, pieces_rects[3])
        ]

        while selected_piece is None:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for piece in chess_pieces:
                        if piece.was_clicked(pygame.mouse.get_pos()):
                            return piece.symbol
                elif event.type == pygame.MOUSEMOTION:
                    for piece in chess_pieces:
                        if piece.rect.collidepoint(pygame.mouse.get_pos()):
                            pygame.draw.rect(
                                top_notification_surface, green, piece.rect, 5)
                        else:
                            pygame.draw.rect(
                                top_notification_surface, black, piece.rect, 5)
                    ui.screen.blit(top_notification_surface, (0, 0))

            for chess_piece in chess_pieces:
                ui.screen.blit(chess_piece.image, chess_piece.rect)

            pygame.display.update()

        return selected_piece
    return promotion_callback


def chosen_difficulty(game_difficulty):
    difficulty_map = {
        0: 'Easy',
        1: 'Medium',
        2: 'Hard',
    }
    return difficulty_map[game_difficulty]


def menu(ui):
    menu = True
    difficulty = False
    quit = False
    font_color = (0, 150, 150)

    # region Main Menu
    menu_options = []

    play_text = 'PLAY ({})'.format(chosen_difficulty(ui.game_difficulty))
    play_menu = ui.font.render(play_text, 1, font_color)
    play_menu_rect = play_menu.get_rect(
        center=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) - 30)
    )

    difficulty_text = 'Difficulty'
    difficulty_menu = ui.font.render(difficulty_text, 1, font_color)
    difficulty_menu_rect = difficulty_menu.get_rect(
        center=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) + 50)
    )
    quit_text = 'Quit'
    quit_menu = ui.font.render(quit_text, 1, font_color)
    quit_menu_rect = quit_menu.get_rect(
        center=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) + 200)
    )
    menu_options.append(
        (play_text, play_menu, play_menu_rect))
    menu_options.append(
        (difficulty_text, difficulty_menu, difficulty_menu_rect))
    menu_options.append(
        (quit_text, quit_menu, quit_menu_rect))
    # endregion

    # region Difficulty Menu
    diff_options = []
    easy_text = 'Easy'
    easy_menu = ui.font.render(easy_text, 1, font_color)
    easy_menu_rect = easy_menu.get_rect(
        center=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) - 30)
    )
    medium_text = 'Medium'
    medium_menu = ui.font.render(medium_text, 1, font_color)
    medium_menu_rect = medium_menu.get_rect(
        center=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) + 50)
    )
    hard_text = 'Hard'
    hard_menu = ui.font.render(hard_text, 1, font_color)
    hard_menu_rect = hard_menu.get_rect(
        center=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) + 130)
    )
    diff_options.append(
        (easy_text, easy_menu, easy_menu_rect))
    diff_options.append(
        (medium_text, medium_menu, medium_menu_rect))
    diff_options.append(
        (hard_text, hard_menu, hard_menu_rect))
    # endregion

    menu_choice = 0
    while menu and not quit:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    menu_choice += 1
                    menu_choice = menu_choice % 3
                if event.key == pygame.K_UP:
                    menu_choice -= 1
                    if menu_choice < 0:
                        menu_choice = 2
                if event.key == pygame.K_RETURN:
                    if difficulty:
                        ui.game_difficulty = menu_choice
                        difficulty = False
                    else:
                        if menu_choice == 0:
                            menu = False
                        if menu_choice == 1:
                            difficulty = True
                        if menu_choice == 2:
                            quit = True
                    menu_choice = 0
            if event.type == pygame.QUIT:
                quit = True

        ui.screen.fill((0, 0, 0,))

        for i in range(3):
            if difficulty:
                text = diff_options[i][0]
                render_text = diff_options[i][1]
                rect = diff_options[i][2]
            else:
                if i == 0:
                    text = 'PLAY ({})'.format(
                        chosen_difficulty(ui.game_difficulty))
                else:
                    text = menu_options[i][0]

                render_text = menu_options[i][1]
                rect = menu_options[i][2]

            if i == menu_choice:
                render_text = ui.font.render(text, 1, Color.RED.rgb)
            else:
                render_text = ui.font.render(text, 1, font_color)

            ui.screen.blit(render_text, rect)
            ui.screen.blit(ui.assets['title'],
                           pygame.Rect(120, 50, 80, 80))
            ui.screen.blit(ui.assets['logo_small'],
                           pygame.Rect(
                               SCREEN_WIDTH - 140,
                               SCREEN_HEIGHT - 80,
                               20, 20)
                           )

        pygame.draw.lines(ui.screen, (0, 128, 255), 1, [
            (0, 0), (SCREEN_WIDTH, 0),
            (SCREEN_WIDTH, SCREEN_HEIGHT), (0, SCREEN_HEIGHT),
        ], 10)

        pygame.display.update()

    return quit


def run_game(ui, game, board):

    held_piece_coord = None
    player_turn = True
    ui.display_text("Your turn...")

    colored_board = []

    game_running = True
    end_game = False

    while game_running:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit = True
                return quit
            if event.type == pygame.KEYDOWN and event.key == \
                    pygame.K_ESCAPE:
                quit = False
                return quit
            if player_turn:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cell_coord = get_coordinates_by_position(
                        pygame.mouse.get_pos(), board)
                    if cell_coord is not None:
                        clicked_piece = \
                            board[cell_coord.row][cell_coord.column]
                        if can_move_piece(clicked_piece, held_piece_coord):
                            held_piece_coord = Coordinate(
                                cell_coord.row, cell_coord.column)
                elif event.type == pygame.MOUSEBUTTONUP:
                    cell_coord = get_coordinates_by_position(
                        pygame.mouse.get_pos(), board)
                    if is_holding_piece(held_piece_coord):
                        dests = destinations(
                            game, held_piece_coord)
                        if cell_coord in dests:
                            move(game, held_piece_coord, cell_coord,
                                 promotion_callback_factory(ui))
                            ui.animate(game.board,
                                       (held_piece_coord, cell_coord))
                            player_turn = False
                            if is_checkmate_for_player(game, Player.BLACK):
                                ui.display_text(
                                    "WHITE player wins! (Press ESC)",
                                    color=(0, 255, 0))
                                end_game = True
                            elif is_check_for_player(game, Player.BLACK):
                                ui.display_text(
                                    "BLACK player is in CHECK",
                                    color=(0, 255, 0))
                            elif is_stalemate_for_player(game, Player.BLACK):
                                ui.display_text(
                                    "Draw by Stalemate!",
                                    color=(255, 0, 0))
                                end_game = True
                            elif is_impossible_checkmate(game):
                                ui.display_text(
                                    "Draw by Impossibility!",
                                    color=(255, 0, 0))
                                end_game = True
                    held_piece_coord = None

        dests = []
        if player_turn and is_holding_piece(held_piece_coord):
            dests = destinations(game, held_piece_coord)
        colored_board = color_board(board, dests)

        if not end_game and not player_turn:
            ui.display_text("Computer turn...")
            movement = greedy_move(game)
            move(game, movement[0], movement[1])
            ui.animate(game.board, movement)
            if is_checkmate_for_player(game, Player.WHITE):
                ui.display_text("BLACK player wins! (Press ESC)",
                                color=(255, 0, 0))
                end_game = True
            elif is_check_for_player(game, Player.WHITE):
                ui.display_text("Your turn... (CHECK!)", color=(255, 0, 0))
            elif is_stalemate_for_player(game, Player.WHITE):
                ui.display_text("Draw by Stalemate!", color=(255, 0, 0))
                end_game = True
            elif is_impossible_checkmate(game):
                ui.display_text("Draw by Impossibility!", color=(255, 0, 0))
                end_game = True
            else:
                ui.display_text("Your turn...")
            player_turn = True

        if end_game:
            player_turn = False
        ui.refresh(board, colored_board)


def run():
    ui = UI()
    running = True
    while running:
        quit = menu(ui)
        if not quit:
            game = Game()
            board = game.board
            quit = run_game(ui, game, board)
            if quit:
                break
            ui.refresh(board, color_board(board, []))
        else:
            break

    pygame.quit()

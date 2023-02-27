import pygame


def draw_board(SCREEN, BOARD_HEIGHT, BOARD_WIDTH, sq_size):
    for x in range(0, BOARD_WIDTH, sq_size):
        for y in range(0, BOARD_HEIGHT, sq_size):
            square = pygame.Rect(x, y, sq_size, sq_size)
            pygame.draw.rect(SCREEN, (0, 0, 0), square, 2)

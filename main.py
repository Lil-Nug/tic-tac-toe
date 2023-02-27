import pygame
from pygame.locals import QUIT
from board import *

pygame.init()

SCREEN_HEIGHT = 750
SCREEN_WIDTH = 1500
BOARD_HEIGHT = 750
BOARD_WIDTH = 750
sq_size = 250

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('toe tac tic')


draw_board(SCREEN, BOARD_HEIGHT, BOARD_WIDTH, sq_size)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()

import pygame
from pygame.locals import *
from board import *
import time

pygame.init()
pygame.font.init()

SCREEN_HEIGHT = 750
SCREEN_WIDTH = 1500
BOARD_HEIGHT = 750
BOARD_WIDTH = 750
sq_size = 250

font = pygame.font.SysFont('Comic Sans MS', 50)


def play_again():
    main()


def main():
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('toe tac tic')
    SCREEN.fill('WHITE')

    images = {}
    for image in ('cross', 'circle'):
        images[image] = pygame.transform.scale(pygame.image.load(
            f'images\\{image}.png').convert_alpha(), (225, 225))

    draw_board(SCREEN, BOARD_HEIGHT, BOARD_WIDTH, sq_size)

    board = [[-1, -1, -1],
             [-1, -1, -1],
             [-1, -1, -1]]

    crossToMove = True
    crossHasWon = None
    moves_done = 0
    running = True
    blank = pygame.Rect(1000, 350, 500, 100)

    while running:
        if crossToMove == True:
            msg = font.render('Cross To Move', False, 'BLACK')
            pygame.draw.rect(SCREEN, (255, 255, 255), blank)
            SCREEN.blit(msg, (1000, 350))
        elif crossToMove == False:
            msg = font.render('Circle To Move', False, 'BLACK')
            pygame.draw.rect(SCREEN, (255, 255, 255), blank)
            SCREEN.blit(msg, (1000, 350))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] < 750 and pos[1] < 750:

                    row = pos[1]//250
                    col = pos[0]//250
                    if board[row][col] == -1:
                        if crossToMove:
                            board[row][col] = 1
                            crossToMove = False
                            moves_done += 1
                            SCREEN.blit(images['cross'],
                                        (col*250+5, row*250+5))
                           # time.sleep(0.25)
                        elif not crossToMove:
                            board[row][col] = 0
                            crossToMove = True
                            moves_done += 1
                            SCREEN.blit(images['circle'],
                                        (col*250+5, row*250+5))
                            # time.sleep(0.25)

                        if board[0][0] == board[1][1] == board[2][2] == 1 or board[0][2] == board[1][1] == board[2][0] == 1:
                            crossHasWon = True
                            break
                        elif board[0][0] == board[1][1] == board[2][2] == 0 or board[0][2] == board[1][1] == board[2][0] == 0:
                            crossHasWon = False
                            break
                        else:
                            for i in range(3):
                                if board[i][0] == board[i][1] == board[i][2] == 1 or board[0][i] == board[1][i] == board[2][i] == 1:
                                    crossHasWon = True
                                    break

                                elif board[i][0] == board[i][1] == board[i][2] == 0 or board[0][i] == board[1][i] == board[2][i] == 0:
                                    crossHasWon = False
                                    break
                            else:
                                continue
                            break
            if crossHasWon == False:
                print('Circle has won')
                win = font.render('Cross has won', False, 'BLACK')
                pygame.draw.rect(SCREEN, (255, 255, 255), blank)
                SCREEN.blit(win, (1000, 350))
                time.sleep(3)
                running = False
                main()

            elif crossHasWon == True:
                print('Cross has won')
                win = font.render('Cross has won', False, 'BLACK')
                pygame.draw.rect(SCREEN, (255, 255, 255), blank)
                SCREEN.blit(win, (1000, 350))
                time.sleep(3)
                running = False
                main()

        pygame.display.update()


if __name__ == '__main__':
    main()

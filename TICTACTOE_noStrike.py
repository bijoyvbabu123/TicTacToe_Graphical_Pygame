# all working with no striking..............
import pygame
from pygame.locals import *
import sys

pygame.init()

# ............................game matrix ....................
b = {7: ' ', 8: ' ', 9: ' ',
     4: ' ', 5: ' ', 6: ' ',
     1: ' ', 2: ' ', 3: ' '}

# ..........................evaluation  N X O D .......................
def evaluate():
    if b[7] == ' ' and b[8] == ' ' and b[9] == ' ' and b[4] == ' ' and b[5] == ' ' and b[6] == ' ' and b[1] == ' ' and \
            b[2] == ' ' and b[3] == ' ':
        return 'N'
    elif b[7] == b[8] == b[9] != ' ':
        return b[7]
    elif b[4] == b[5] == b[6] != ' ':
        return b[4]
    elif b[1] == b[2] == b[3] != ' ':
        return b[1]
    elif b[7] == b[4] == b[1] != ' ':
        return b[7]
    elif b[8] == b[5] == b[2] != ' ':
        return b[8]
    elif b[9] == b[6] == b[3] != ' ':
        return b[9]
    elif b[7] == b[5] == b[3] != ' ':
        return b[7]
    elif b[9] == b[5] == b[1] != ' ':
        return b[9]
    elif b[7] != ' ' and b[8] != ' ' and b[9] != ' ' and b[4] != ' ' and b[5] != ' ' and b[6] != ' ' and \
            b[1] != ' ' and b[2] != ' ' and b[3] != ' ':
        return 'D'
    else:
        return 'N'


# ...................................colors............................................
BLACK = (0, 0, 0)
RED = (255, 0, 0)  # X
BLUE = (0, 255, 255)  # o
YELLOW = (255, 255, 0)  # table         background black
AQUA = (0, 255, 255)  # buttons
ORANGE = (255, 100, 0)  # Winner
# ............................................................setting display..................................
gamedisplay = pygame.display.set_mode((900, 650), 0, 32)
pygame.display.set_caption('TicTacToe')
gamedisplay.fill(BLACK)
# .................................................all the  boxes needed ....................................
box = {7: pygame.Rect(50, 50, 150, 150), 8: pygame.Rect(201, 50, 150, 150), 9: pygame.Rect(352, 50, 150, 150),
       4: pygame.Rect(50, 201, 150, 150), 5: pygame.Rect(201, 201, 150, 150), 6: pygame.Rect(352, 201, 150, 150),
       1: pygame.Rect(50, 352, 150, 150), 2: pygame.Rect(201, 352, 150, 150), 3: pygame.Rect(352, 352, 150, 150)}
newbutton = pygame.Rect(650, 100, 200, 100)
quitbutton = pygame.Rect(650, 350, 200, 100)
winerase = pygame.Rect(50, 530, 800, 120)
# ..............................................................drawing box and buttons...........................
for i in range(1, 10):
    pygame.draw.rect(gamedisplay, YELLOW, box[i], 5)
pygame.draw.rect(gamedisplay, AQUA, quitbutton)
pygame.draw.rect(gamedisplay, AQUA, newbutton)
# .......................................................font objects needed...........................................
buttonsfontobj = pygame.font.Font('arial.ttf', 70)
xofontobj = pygame.font.Font('TEMPSITC.TTF', 110)
winfontobj = pygame.font.Font('TEMPSITC.TTF', 70)
# ...........................................................adding text to the buttons............................
textquitsurfaceobj = buttonsfontobj.render('QUIT', True, BLACK)
textnewsurfaceobj = buttonsfontobj.render('NEW', True, BLACK)
gamedisplay.blit(textquitsurfaceobj, (quitbutton.left + 15, quitbutton.top + 15))
gamedisplay.blit(textnewsurfaceobj, (newbutton.left + 20, newbutton.top + 20))
# ............................................V A R I A B L E S................................
p = 0
winner = 'N'
#  ..................................G A M E L O O P..........................................
pygame.event.clear()
while True:

    event = pygame.event.wait()

    winner = evaluate()

    for i in range(1, 10):
        if b[i] == 'X':
            xoobj = xofontobj.render(b[i], True, RED)
        else:
            xoobj = xofontobj.render(b[i], True, BLUE)
        xorect = xoobj.get_rect()
        xorect.center = box[i].center
        gamedisplay.blit(xoobj, xorect)

    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1 and quitbutton.left <= \
            pygame.mouse.get_pos()[0] <= quitbutton.right \
            and quitbutton.top <= pygame.mouse.get_pos()[1] <= quitbutton.bottom:
        pygame.quit()
        sys.exit()

    if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1 and newbutton.left <= \
            pygame.mouse.get_pos()[0] <= newbutton.right \
            and newbutton.top <= pygame.mouse.get_pos()[1] <= newbutton.bottom:
        p = 0
        winner = 'N'
        pygame.draw.rect(gamedisplay, BLACK, winerase)
        for i in range(1, 10):
            b[i] = ' '
            pygame.draw.rect(gamedisplay, BLACK, box[i])
            pygame.draw.rect(gamedisplay, YELLOW, box[i], 5)

    if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1 and winner == 'N':
        key = 0
        for i in range(1, 10):
            if box[i].left <= pygame.mouse.get_pos()[0] <= box[i].right and \
                    box[i].top <= pygame.mouse.get_pos()[1] <= box[i].bottom and b[i] == ' ':
                key: int = i
                break
        if 0 < key < 10:
            if p == 0:
                b[key] = 'X'
                p = 1
            else:
                b[key] = 'O'
                p = 0

    if winner != 'N':
        if winner == 'D':
            winsurfaceobj = winfontobj.render(' D R A W ', True, ORANGE)
        else:
            winsurfaceobj = winfontobj.render(winner+'   W I N S ', True, ORANGE)
        winrect = winsurfaceobj.get_rect()
        winrect.center = (275, 600)
        gamedisplay.blit(winsurfaceobj, winrect)

    pygame.display.update()

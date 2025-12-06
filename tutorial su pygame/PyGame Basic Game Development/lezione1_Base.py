import pygame
#import sys
#import time

pygame.init()

# pygame.display.init()
#size = (int(sys.argv[1]), int(sys.argv[2]))
#FINESTRA = pygame.display.set_mode(size)

#pygame.display.set_caption(sys.argv[0])

#time.sleep(2)

ALTEZZA = 800
LARGHEZZA = 400
TITOLO = 'Le basi di pyGame'

ROSSO = (255, 0, 0)
BLUE = (0, 0, 255)

FINESTRA = pygame.display.set_mode((ALTEZZA, LARGHEZZA))
pygame.display.set_caption(TITOLO)
FINESTRA.fill(ROSSO)

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    
    surf0 = pygame.Surface((100, 100))
    surf1 = pygame.Surface((50, 50))
    surf1.fill(BLUE)

    surf0.blit(surf1, (0, 0))
    FINESTRA.blit(surf0, (100, 100))

    pygame.display.update()
    #time.sleep(2)

pygame.quit()
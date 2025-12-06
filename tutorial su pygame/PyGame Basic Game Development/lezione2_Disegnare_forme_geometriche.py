import pygame

pygame.init()

ALTEZZA = 800
LARGHEZZA = 400
TITOLO = 'Disegnare dei poligoni sullo schermo'

ROSSO = (255, 0, 0)
BLUE = (0, 0, 255)
VERDE = (0, 255, 0)
NERO = (0, 0, 0)

FINESTRA = pygame.display.set_mode((ALTEZZA, LARGHEZZA))
pygame.display.set_caption(TITOLO)




loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    FINESTRA.fill(NERO)
    pygame.draw.circle(FINESTRA, VERDE, (25, 25), 25)

    pygame.display.update()

pygame.quit()
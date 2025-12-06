import pygame

pygame.init()

ALTEZZA = 800
LARGHEZZA = 400
TITOLO = 'La gestione degli immagini'

NERO = (0, 0, 0)

FINESTRA = pygame.display.set_mode((ALTEZZA, LARGHEZZA))
pygame.display.set_caption(TITOLO)
FINESTRA.fill(NERO)

foto1 = 'immagini/immagi1.png'
imag = pygame.image.load(foto1)

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    
    FINESTRA.blit(imag, (100, 100))
    
    pygame.display.update()

pygame.quit()
import pygame

pygame.init()

ALTEZZA = 800
LARGHEZZA = 400
TITOLO = 'La gestione dei tasti'

NERO = (0, 0, 0)
BIANCO = (255, 255, 255)

FINESTRA = pygame.display.set_mode((ALTEZZA, LARGHEZZA))
pygame.display.set_caption(TITOLO)
FINESTRA.fill(NERO)

clock = pygame.time.Clock()

lettera = 'immagini/immagi1.png'
A = pygame.image.load(lettera)

loop = True
while loop:
    FINESTRA.fill(NERO)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            print('lettera ' + str(event.key) + ' aka ' + pygame.key.name(event.key) + " down")
        if event.type == pygame.KEYUP:
            print('lettera ' + str(event.key) + ' aka ' + pygame.key.name(event.key) + " up")
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        FINESTRA.blit(A, (0, 0))
    
    pygame.display.update()
    
    clock.tick_busy_loop(60)

pygame.quit()
"""9. Mostrare la posizione del mouse
Mostra sullo schermo, tramite testo 
renderizzato, la posizione corrente 
del cursore. Aggiornala ogni frame."""

import pygame

pygame.init()

LARGHEZZA = 800
ALTEZZA = 600
TITOLO = 'Mostrare la posizione del mouse'

BIANCO = (255, 255, 255)
NERO = (0, 0, 0)

font = pygame.font.SysFont('Arial', 60, bold=True, italic=False)

clock = pygame.time.Clock()
FPS = 60 

schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption(TITOLO)

loop = True
while loop:
    clock.tick(FPS)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop = False
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    text = font.render(f"Posizione cursore: {mouse_x}, {mouse_y}", 
                       True, (255, 255, 255))
        
    schermo.fill(NERO)
    schermo.blit(text, (20, 20))
    
    pygame.display.update()

pygame.quit()
import pygame

pygame.init()

ALTEZZA = 800
LARGHEZZA = 400
TITOLO = 'La gestione del Clock e degli eventi e uso di font'

NERO = (0, 0, 0)
BIANCO = (255, 255, 255)

pos_call = (0, 0)
pos_even = (0, 0)

font = pygame.font.SysFont('monospace', 25)

FINESTRA = pygame.display.set_mode((ALTEZZA, LARGHEZZA))
pygame.display.set_caption(TITOLO)
FINESTRA.fill(NERO)

clock = pygame.time.Clock()

loop = True
while loop:
    FINESTRA.fill(NERO)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.MOUSEMOTION:
            pos_even = event.pos
            
    pos_call = pygame.mouse.get_pos()
    string = font.render(" pos_even = " + str(pos_even) + 
                         " pos_call = " + str(pos_call), 1, BIANCO)
    
    FINESTRA.blit(string, pos_even)
    pygame.display.update()
    clock.tick_busy_loop(60)

pygame.quit()
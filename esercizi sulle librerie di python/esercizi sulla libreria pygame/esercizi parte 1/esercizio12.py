"""12. Movimento continuo orizzontale/verticale
Implementa dei pulsanti che attivano spostamenti 
interni allo schermo: premi “d” per far muovere 
un quadrato automaticamente a destra, “a” per 
sinistra, “s” per fermarlo."""

import pygame

pygame.init()

LARGHEZZA = 800
ALTEZZA = 600
TITOLO = 'Movimento continuo orizzontale/verticale'

BIANCO = (255, 255, 255)
NERO = (0, 0, 0)

clock = pygame.time.Clock()
FPS = 60 

schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption(TITOLO)


x = 100
y = 100
quadrato = 100
spinta = 0

loop = True
while loop:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop = False
    
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_d:
                spinta = 5
            if evento.key == pygame.K_a:
                spinta = -5
            if evento.key == pygame.K_s:
                spinta = 0
    
    x += spinta
    
    schermo.fill(NERO)
    pygame.draw.rect(schermo, BIANCO, (x, y, quadrato, quadrato))
    
    pygame.display.update()
    
pygame.quit()
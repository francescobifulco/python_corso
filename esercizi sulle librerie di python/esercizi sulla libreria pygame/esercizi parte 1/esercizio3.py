"""3. Disegnare forme semplici sullo schermo
Disegna diversi elementi geometrici: un 
rettangolo, un cerchio, una linea e un 
poligono. Posizionali in punti diversi 
della finestra. Mantieni tutto visibile 
tramite il loop principale.
"""

import pygame

pygame.init()

LARGHEZZA = 800
ALTEZZA = 600
TITOLO = 'Disegnare forme semplici sullo schermo'

BIANCO = (255, 255, 255)
ROSSO = (255, 0, 0)
BLU = (0, 0, 255)
NERO = (0, 0, 0)
VERDE = (50, 168, 82)

schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption(TITOLO)

loop = True
while loop:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop = False
    
    schermo.fill(NERO)
    
    rettangolo = (10, 10, 100, 50)
    pygame.draw.rect(schermo, ROSSO, rettangolo, 0)
    
    cerchio = (60, 120)
    raggio = 50
    pygame.draw.circle(schermo, BLU, cerchio, raggio, 0)
    
    pygame.draw.line(schermo, BIANCO, (10, 200), (100, 200), 20)
    
    vertici = [(300, 200),   # vertice sinistro
               (450, 100),   # vertice alto
               (600, 200)]    # vertice destro]
    pygame.draw.polygon(schermo, VERDE, vertici, 0)
    
    pygame.display.flip()

pygame.quit()
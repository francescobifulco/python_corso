"""4. Disegnare una griglia
Scrivi un programma che 
disegna una griglia 20×20 sullo 
schermo (con spazi regolari). I 
valori della griglia devono 
essere calcolati tramite cicli, 
non scritti manualmente."""

import pygame

pygame.init()

LARGHEZZA = 800
ALTEZZA = 600
TITOLO = 'Disegnare una griglia'

# Calcolo della distanza tra le linee
spaziatura_x = LARGHEZZA // 20
spaziatura_y = ALTEZZA // 20

GRIGIO = (200, 200, 200)

schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption(TITOLO)

loop = True
while loop:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop = False
    
    schermo.fill((0, 0, 0))  # pulisce lo schermo
    
    for i in range(21):
        x = i * spaziatura_x
        pygame.draw.line(schermo, GRIGIO, (x, 0), (x, ALTEZZA))
    
    for j in range(21):
        y = j * spaziatura_y
        pygame.draw.line(schermo, GRIGIO, (0, y), (LARGHEZZA, y))
                
    pygame.display.update()
    
pygame.quit()
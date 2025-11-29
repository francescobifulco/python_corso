"""8. Rilevare clic del mouse
Disegna un cerchio fisso sullo 
schermo. Ogni volta che l’utente 
clicca con il mouse all’interno 
del cerchio, cambia colore."""

import pygame
import math

pygame.init()

LARGHEZZA = 800
ALTEZZA = 600
TITOLO = 'Rilevare clic del mouse'

BIANCO = (255, 255, 255)
NERO = (0, 0, 0)
ROSSO = (255, 0, 0)
BLU = (0, 0, 255)
VERDE = (0, 255, 0)
colore = BIANCO

def click_in_cerchio(x, y):
    distanza = math.sqrt((x - cerchio_x)**2 + (y - cerchio_y)**2)
    return distanza <= raggio

clock = pygame.time.Clock()
FPS = 60 

schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption(TITOLO)

cerchio_x = 400
cerchio_y = 300
raggio = 50


loop = True
while loop:
    clock.tick(FPS)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop = False
        
        
        if evento.type == pygame.MOUSEBUTTONDOWN:  # Premuto
            if click_in_cerchio(evento.pos[0], evento.pos[1]):
                if evento.button == 1:  # Pulsante sinistro
                   print("Click sinistro!")
                   colore = ROSSO
                elif evento.button == 2:  # Pulsante centrale
                   print("Click centrale!")
                   colore = BLU
                elif evento.button == 3:  # Pulsante destro
                   print("Click destro!")
                   colore = VERDE
        elif evento.type == pygame.MOUSEBUTTONUP:  # Rilasciato
            print("Pulsante rilasciato")

    schermo.fill(NERO)
    pygame.draw.circle(schermo, colore, (cerchio_x, cerchio_y), raggio)
    
    pygame.display.update()

pygame.quit()

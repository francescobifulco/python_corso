"""1. Inizializzazione di Pygame e finestra base
Crea un programma che inizializzi Pygame, apra una finestra di dimensioni 
800×600, imposti un titolo personalizzato e mostri uno sfondo di colore a 
tua scelta. Mantieni la finestra aperta tramite un loop principale che 
termina quando viene premuto il tasto X della finestra."""

import pygame

pygame.init()

LARGHEZZA = 800
ALTEZZA = 600
TITOLO = 'Inizializzazione di Pygame e finestra base'

schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption(TITOLO)

ROSSO = (255, 0, 0)

loop = True
while loop:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop = False
        
    schermo.fill(ROSSO)
    pygame.display.flip()

pygame.quit()
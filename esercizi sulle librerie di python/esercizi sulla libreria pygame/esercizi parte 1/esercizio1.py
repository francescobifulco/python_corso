"""1. Creare una finestra Pygame**
Obiettivo: capire l’inizializzazione del modulo.
Descrizione: crea una finestra 800×600 con titolo personalizzato e ciclo principale.
Extra: cambia colore dello sfondo ogni 2 secondi."""

import pygame

pygame.init()

LARGHEZZA = 800
ALTEZZA = 600
TITOLO = 'personalizzato e ciclo principale'

CHANGE_COLOR = pygame.USEREVENT
pygame.time.set_timer(CHANGE_COLOR, 2000)

# Colori
BIANCO = (255, 255, 255)
ROSSO = (255, 0, 0)

# Colore iniziale
colore_corrente = BIANCO

clock = pygame.time.Clock()


schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption(TITOLO)

loop = True
while loop:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop = False
        if evento.type == CHANGE_COLOR:
            colore_corrente = ROSSO if colore_corrente == BIANCO else BIANCO
    
    # Disegno
    schermo.fill(colore_corrente)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
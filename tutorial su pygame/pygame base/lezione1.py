import pygame
from pygame.locals import *
from sys import exit

# Inizializza tutti i moduli di Pygame
pygame.init()

# Crea una finestra 640x480, con profondità di colore predefinita
screen = pygame.display.set_mode((640, 480), 0, 32)

# Imposta il titolo della finestra
pygame.display.set_caption('Lezione 1')

# Carica l'immagine di sfondo e la converte per velocizzare il rendering
background = pygame.image.load('immaggini/sfondolez.jpg').convert()

# Carica l'immagine del cursore del mouse con il canale alpha (trasparenza)
mouse_cursor = pygame.image.load('immaggini/mouse_cursor.jpg').convert_alpha()

# Ciclo principale del gioco / programma
while True:
    # Gestione degli eventi (chiusura finestra, input, ecc.)
    for event in pygame.event.get():
        if event.type == QUIT:   # Evento quando si chiude la finestra
            exit()              # Termina il programma

    # Disegna l'immagine di sfondo nella posizione (0,0)
    screen.blit(background, (0, 0))

    # Ottiene la posizione corrente del mouse
    x, y = pygame.mouse.get_pos()

    # Centra l'immagine del cursore sulla posizione del mouse
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2

    # Disegna l'immagine del cursore del mouse nella posizione modificata
    screen.blit(mouse_cursor, (x, y))

    # Aggiorna lo schermo con tutte le modifiche effettuate
    pygame.display.update()
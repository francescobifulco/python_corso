import pygame
from pygame.locals import *
from sys import exit

# Inizializza tutti i moduli di Pygame
pygame.init()

# Crea una finestra 640x480, con profondità di colore predefinita
screen = pygame.display.set_mode((640, 480), 0, 32)

# Carica l'immagine di sfondo e la converte per velocizzare il rendering
background = pygame.image.load('immaggini/sfondolez.jpg').convert()

# Imposta il titolo della finestra
pygame.display.set_caption('Lezione 2')

# Posizione iniziale dello sfondo
x, y = 0, 0

# Variabili che servono a modificare la 
# posizione (velocità del movimento)
muovi_x, muovi_y = 0, 0

# Ciclo principale del gioco (loop infinito)
while True:
    # Gestione degli eventi (tastiera, mouse, chiusura finestra)
    for event in pygame.event.get():
        
        # Se l’utente chiude la finestra, termina il programma
        if event.type == QUIT:
            exit()

        # Rileva la pressione dei tasti
        if event.type == KEYDOWN:
            # Freccia sinistra → muove a sinistra
            if event.key == K_LEFT:
                muovi_x -= 1
            # Freccia destra → muove a destra
            elif event.key == K_RIGHT:
                muovi_x += 1
            # Freccia su → muove verso l’alto
            elif event.key == K_UP:
                muovi_y -= 1
            # Freccia giù → muove verso il basso
            elif event.key == K_DOWN:
                muovi_y += 1

        # Rileva il rilascio dei tasti
        if event.type == KEYUP:
            # Se rilascio freccia sinistra → stop movimento orizzontale
            if event.key == K_LEFT:
                muovi_x = 0
            # Se rilascio freccia destra
            elif event.key == K_RIGHT:
                muovi_x = 0
            # Se rilascio freccia su → stop movimento verticale
            elif event.key == K_UP:
                muovi_y = 0
            # Se rilascio freccia giù
            elif event.key == K_DOWN:
                muovi_y = 0

    # Aggiorna la posizione dello sfondo in base alla direzione
    x += muovi_x
    y += muovi_y

    # Riempie lo schermo di nero per cancellare il frame precedente
    screen.fill((0, 0, 0))
    
    # Disegna l'immagine di sfondo alla nuova posizione
    screen.blit(background, (x, y))

    # Aggiorna lo schermo con tutto ciò che è stato disegnato
    pygame.display.update()
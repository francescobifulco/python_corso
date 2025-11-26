import pygame
from pygame.locals import *
from sys import exit

# Inizializza tutti i moduli di Pygame
pygame.init()

# Crea una finestra ridimensionabile (flag RESIZABLE)
SCREEN_SIZE = (640, 480) # Dimensione iniziale della finestra
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

# Carica l'immagine di sfondo e la converte per velocizzare il rendering
background = pygame.image.load('immaggini/sfondolez.jpg').convert()

# Imposta il titolo della finestra
pygame.display.set_caption('Lezione 4')



while True:
    # Attende un evento (bloccante, risparmia CPU)
    event = pygame.event.wait()
    if event.type == QUIT:
        exit()
    # Quando la finestra viene ridimensionata
    if event.type == VIDEORESIZE:
        # Aggiorna la dimensione interna
        SCREEN_SIZE = event.size
        
        # Crea una nuova finestra con la nuova dimensione
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

        # Aggiorna il titolo mostrando la nuova dimensione
        pygame.display.set_caption('Window resized to ' + str(event.size))

    # Estrae le dimensioni aggiornate della finestra
    screen_width, screen_height = SCREEN_SIZE

    # Riempie l'intera area della finestra con "tessere" dello sfondo
    # È un "tiling": ripete l'immagine in X e Y per riempire tutto
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))
            
    pygame.display.update()
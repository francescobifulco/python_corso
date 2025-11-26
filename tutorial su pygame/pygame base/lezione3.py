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
pygame.display.set_caption('Lezione 3')

# Variabile che indica se la modalità fullscreen è attiva
fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        
        # Controlla se un tasto è stato premuto
        if event.type == KEYDOWN:
            # Se viene premuto il tasto 
            # 'f' → attiva o disattiva fullscreen
            if event.key == K_f:
                # Inverte lo stato (True/False)
                fullscreen = not fullscreen
            # Se FULLSCREEN è True → attiva la modalità a schermo intero
            if fullscreen:
                # Il secondo parametro indica la modalità: 
                # qui FULLSCREEN = True viene interpretato come FLAG 1
                screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
            else:
                # Modalità finestra normale
                screen = pygame.display.set_mode((640, 480), 0, 32)
    
    screen.blit(background, (0,0))
    pygame.display.update()
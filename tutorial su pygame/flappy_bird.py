# Importo le Librerie
import pygame
import random

# Inizializzo PyGame
pygame.init()

# Carico le Immagini
sfondo = pygame.image.load('immagini/sfondo.png')
uccello = pygame.image.load('immagini/uccello.png')
base = pygame.image.load('immagini/base.png')
gameover = pygame.image.load('immagini/gameover.png')
tubo_giu = pygame.image.load('immagini/tubo.png')
tubo_su = pygame.transform.flip(tubo_giu, False, True)

# Costani Globali
SCHERMO = pygame.display.set_mode((288, 512))
FPS = 50

def disegna_oggetti():
    SCHERMO.blit(sfondo, (0,0))
    SCHERMO.blit(uccello, (uccellox,uccelloy))

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def inizializza():
    global uccellox, uccelloy, uccello_vely
    uccellox, uccelloy = 60, 150
    uccello_vely = 0
    
inizializza()

while True:
    uccello_vely += 1
    uccelloy += uccello_vely
    
    disegna_oggetti()
    aggiorna()
    
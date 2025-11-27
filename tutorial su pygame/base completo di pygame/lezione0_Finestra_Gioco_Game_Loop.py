# Importazione
import pygame

# Inizializzazione
pygame.init()

# Creazione della Finestra di Gioco
larghezza = 800
altezza = 400
screen = pygame.display.set_mode((larghezza, altezza))
colore = (252, 186, 3)
# Impostazione del titolo della finestra
pygame.display.set_caption('La Finestra di Gioco e il Game Loop')

# Il concetto di FPS (Frame per Secondo) e la gestione del tempo
FPS = 50
clock = pygame.time.Clock()
clock.tick(FPS)

# Aggiornamento dello Schermo
screen.fill(colore)

# Il Ciclo di Gioco
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    
    # Aggiornamento schermo, logica di gioco, disegni, ecc.
    pygame.display.update()
    clock.tick(FPS)
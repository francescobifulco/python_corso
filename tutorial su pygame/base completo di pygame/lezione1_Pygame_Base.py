import pygame
import sys # Modulo necessario per la chiusura corretta

# 1. Inizializzazione di Pygame
pygame.init()

# Definizione delle costanti
LARGHEZZA = 800
ALTEZZA = 600
TITOLO = "Pygame Base"

# 2. Creazione della Finestra
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption(TITOLO)

# Colore di sfondo (RGB)
NERO = (0, 0, 0)

# 3. Game Loop
running = True
while running:
    # 4. Gestione degli Eventi
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            # Imposta running a False per uscire dal loop
            running = False 

    # 5. Disegno / Rendering
    schermo.fill(NERO) # Riempie lo sfondo

    # Aggiorna lo schermo per rendere visibili i cambiamenti
    pygame.display.flip()

# 6. Uscita
pygame.quit()
sys.exit()
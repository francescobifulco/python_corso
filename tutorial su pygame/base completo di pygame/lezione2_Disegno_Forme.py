import pygame

pygame.init()

LARGHEZZA, ALTEZZA = 800, 600
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Disegno Forme")

# Colori
BIANCO = (255, 255, 255)
ROSSO = (255, 0, 0)
BLU = (0, 0, 255)
NERO = (0, 0, 0)

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    schermo.fill(NERO)

    # Disegna un rettangolo: 
    # pygame.draw.rect(superficie, 
    # colore, (x, y, larghezza, altezza), spessore)
    # Spessore 0 significa riempito
    rettangolo_pos = (50, 50, 100, 50)
    pygame.draw.rect(schermo, ROSSO, rettangolo_pos, 0)

    # Disegna un cerchio: 
    # pygame.draw.circle(superficie, 
    # colore, (centro_x, centro_y), raggio, spessore)
    centro_cerchio = (400, 300)
    raggio = 50
    pygame.draw.circle(schermo, BLU, centro_cerchio, raggio, 0)

    # Aggiorna lo schermo
    pygame.display.flip()

pygame.quit()
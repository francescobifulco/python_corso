import pygame
import math

pygame.init()

LARGHEZZA = 800
ALTEZZA = 600
NERO = (0, 0, 0)

schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
clock = pygame.time.Clock()

# Carica immagine astronave
img = pygame.image.load('./immaggini/player.png').convert_alpha()

# Posizione e variabili
x, y = 400, 300
angolo = 0
velocita = 5

loop = True
while loop:
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop = False

    tasti = pygame.key.get_pressed()

    # Rotazione
    if tasti[pygame.K_LEFT]:
        angolo += 4
    if tasti[pygame.K_RIGHT]:
        angolo -= 4

    # Movimento nella direzione dell’angolo
    if tasti[pygame.K_UP]:
        # Calcolo vettore direzionale
        dx = math.cos(math.radians(angolo))
        dy = -math.sin(math.radians(angolo))

        x += dx * velocita
        y += dy * velocita

    # Rotazione immagine mantenendo il centro
    img_rot = pygame.transform.rotate(img, angolo)
    rect = img_rot.get_rect(center=(x, y))

    schermo.fill(NERO)
    schermo.blit(img_rot, rect)
    pygame.display.update()

pygame.quit()

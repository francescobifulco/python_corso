import pygame
import sys

pygame.init()

# --- Setup finestra ---
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movimento automatico")

clock = pygame.time.Clock()

# --- Proprietà del quadrato ---
x = 100
y = 180
size = 40
speed = 0   # velocità orizzontale

running = True
while running:
    clock.tick(60)  # 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # --- Controllo tasti ---
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                speed = 5      # muove a destra
            if event.key == pygame.K_a:
                speed = -5     # muove a sinistra
            if event.key == pygame.K_s:
                speed = 0      # si ferma

    # --- Aggiorna posizione ---
    x += speed

    # Limiti schermo (opzionali)
    if x < 0:
        x = 0
    if x + size > WIDTH:
        x = WIDTH - size

    # --- Disegno ---
    screen.fill((30, 30, 30))                     # sfondo
    pygame.draw.rect(screen, (200, 50, 50), (x, y, size, size))  # quadrato

    pygame.display.flip()

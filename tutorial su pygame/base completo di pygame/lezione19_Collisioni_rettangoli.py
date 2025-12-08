# Le collisioni più semplici in Pygame utilizzano 
# gli oggetti pygame.Rect, che rappresentano 
# rettangoli con posizione e dimensioni.

import pygame

pygame.init()

FINESTRA = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Collisioni tra rettangoli')
clock = pygame.time.Clock()

NERO = (30, 30, 30)
VERDE = (0, 255, 0)
ROSSO = (255, 0, 0)


giocattore = pygame.Rect(50, 50, 50, 50)
nemico = pygame.Rect(300, 150, 60, 60)

velocita = 5

loop = True

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]: giocattore.x += velocita
    if keys[pygame.K_LEFT]:  giocattore.x -= velocita
    if keys[pygame.K_UP]:    giocattore.y -= velocita
    if keys[pygame.K_DOWN]:  giocattore.y += velocita
    
    # --- Collisione ---
    if giocattore.colliderect(nemico):
        print("Collisione!")
    
    FINESTRA.fill(NERO)
    pygame.draw.rect(FINESTRA, VERDE, giocattore)
    pygame.draw.rect(FINESTRA, ROSSO, nemico)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
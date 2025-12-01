"""14. Spostamento di un'immagine con rotazione alle frecce
Muovi un'immagine nella direzione in cui è ruotata 
(simile a un’astronave). Usa un vettore direzionale 
basato sull’angolo."""

import pygame
import math

pygame.init()

LARGHEZZA = 800
ALTEZZA = 600
TITOLO = 'Spostamento di un immagine con rotazione alle frecce'

NERO = (0, 0, 0)
angolo = 0
posizione = (300, 200)

clock = pygame.time.Clock()
FPS = 60 

schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption(TITOLO)

img_path = 'immagine/player.png'
img = pygame.image.load(img_path).convert_alpha()

x, y = 400, 300
angolo = 0
velocita = 5

loop = True
while loop:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop = False
    
    tasti = pygame.key.get_pressed()
    
    if tasti[pygame.K_LEFT]:
        angolo += 3
    if tasti[pygame.K_RIGHT]:
        angolo -= 3 
    
    if tasti[pygame.K_UP]:
        dx = math.cos(math.radians(angolo))
        dy = -math.sin(math.radians(angolo))

        x += dx * velocita
        y += dy * velocita
        
    img_rot = pygame.transform.rotate(img, angolo)
    rect = img_rot.get_rect(center=(x, y))
    
    schermo.fill(NERO)
    schermo.blit(img_rot, rect)
        
    pygame.display.update()
    
pygame.quit()
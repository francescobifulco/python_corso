"""13. Rotazione di un'immagine
Carica un’immagine (per es. un player) 
e ruotala quando il giocatore preme i 
tasti ← e →. Mantieni il centro 
dell’immagine costante."""

import pygame

pygame.init()

LARGHEZZA = 800
ALTEZZA = 600
TITOLO = 'Rotazione di un immagine'

NERO = (0, 0, 0)
angolo = 0
posizione = (300, 200)

clock = pygame.time.Clock()
FPS = 60 

schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption(TITOLO)

img_path = 'immagine/player.png'
img = pygame.image.load(img_path).convert_alpha()

loop = True
while loop:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop = False
    
    tasti = pygame.key.get_pressed()
    
    if tasti[pygame.K_LEFT]:
        angolo += 3        # ruota antiorario
    if tasti[pygame.K_RIGHT]:
        angolo -= 3 
        
    img_rot = pygame.transform.rotate(img, angolo)
    # mantieni il centro dell'immagine costante
    rect = img_rot.get_rect(center=posizione)
    
    schermo.fill(NERO)
    schermo.blit(img_rot, rect)
        
    pygame.display.update()
    
pygame.quit()
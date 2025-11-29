"""5. Spostamento di un punto con le frecce
Disegna un piccolo cerchio che rappresenta 
un punto. Permetti all’utente di muoverlo 
con le frecce direzionali, aggiornando ad 
ogni frame la sua posizione."""

import pygame

pygame.init()

LARGHEZZA = 800
ALTEZZA = 600
TITOLO = 'Spostamento di un punto con le frecce'

BIANCO = (255, 255, 255)
NERO = (0, 0, 0)

clock = pygame.time.Clock()
FPS = 60 

schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption(TITOLO)

cerchio_x = 400
cerchio_y = 300
raggio = 50
cerchio_vel = 5

loop = True
while loop:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop = False
    
    tasti_premuti = pygame.key.get_pressed()
        
    if tasti_premuti[pygame.K_LEFT]:
        cerchio_x -= cerchio_vel
    if tasti_premuti[pygame.K_RIGHT]:
        cerchio_x += cerchio_vel
    if tasti_premuti[pygame.K_UP]:
        cerchio_y -= cerchio_vel
    if tasti_premuti[pygame.K_DOWN]:
        cerchio_y += cerchio_vel
        
    cerchio_x = max(raggio, min(cerchio_x, LARGHEZZA - raggio))
    cerchio_y = max(raggio, min(cerchio_y, ALTEZZA - raggio))
    
    schermo.fill(NERO)
    pygame.draw.circle(schermo, BIANCO, (cerchio_x, cerchio_y), raggio, 0)
    
    pygame.display.update()
    
pygame.quit()
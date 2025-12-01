"""10. Movimento con attrito
Crea un oggetto che continua 
a muoversi anche dopo aver 
rilasciato i tasti, rallentando 
gradualmente grazie a un attrito 
simulato."""

import pygame

pygame.init()

LARGHEZZA = 800
ALTEZZA = 600
TITOLO = 'Movimento con attrito'

BIANCO = (255, 255, 255)
NERO = (0, 0, 0)

clock = pygame.time.Clock()
FPS = 60 

schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption(TITOLO)

cerchio_x = 400
cerchio_y = 300
raggio = 50

cerchio_vel_x = 0
cerchio_vel_y = 0
attrito = 0.95
spinta = 1

loop = True
while loop:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop = False
    
    tasti_premuti = pygame.key.get_pressed()

    if tasti_premuti[pygame.K_LEFT]:
        cerchio_vel_x -= spinta
    if tasti_premuti[pygame.K_RIGHT]:
        cerchio_vel_x += spinta
    if tasti_premuti[pygame.K_UP]:
        cerchio_vel_y -= spinta
    if tasti_premuti[pygame.K_DOWN]:
        cerchio_vel_y += spinta
    
    cerchio_vel_x *= attrito
    cerchio_vel_y *= attrito
    
    if abs(cerchio_vel_x) < 0.05:
        cerchio_vel_x = 0
    if abs(cerchio_vel_y) < 0.05:
        cerchio_vel_y = 0
    
    cerchio_x += cerchio_vel_x
    cerchio_y += cerchio_vel_y
        
    cerchio_x = max(raggio, min(cerchio_x, LARGHEZZA - raggio))
    cerchio_y = max(raggio, min(cerchio_y, ALTEZZA - raggio))
    
    schermo.fill(NERO)
    pygame.draw.circle(schermo, BIANCO, (int(cerchio_x), int(cerchio_y)), raggio)
    
    pygame.display.update()
    
pygame.quit()
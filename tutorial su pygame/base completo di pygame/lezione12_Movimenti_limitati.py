import pygame

pygame.init()

LARGHEZZA = 800
ALTEZZA = 600
TITOLO = 'Movimento limitato ai bordi'

BIANCO = (255, 255, 255)
NERO = (0, 0, 0)

clock = pygame.time.Clock()
FPS = 60 

schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption(TITOLO)

cerchio_x = 400
cerchio_y = 300
raggio = 50

vel_x = 0
vel_y = 0
spinta = 5

loop = True
while loop:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop = False
    
    tasti_premuti = pygame.key.get_pressed()
    
    if tasti_premuti[pygame.K_LEFT]:
        vel_x = -spinta
    elif tasti_premuti[pygame.K_RIGHT]:
        vel_x = spinta
    else:
        vel_x = 0
    
    if tasti_premuti[pygame.K_UP]:
        vel_y = -spinta
    elif tasti_premuti[pygame.K_DOWN]:
        vel_y = spinta
    else:
        vel_y = 0
    
    if cerchio_x - raggio < 0:
        cerchio_x = raggio
        vel_x = 0
    if cerchio_x + raggio > LARGHEZZA:
        cerchio_x = LARGHEZZA - raggio
        vel_x = 0
        
    cerchio_x += vel_x
    cerchio_y += vel_y

    if cerchio_y - raggio < 0:
        cerchio_y = raggio
        vel_y = 0
    if cerchio_y + raggio > ALTEZZA:
        cerchio_y = ALTEZZA - raggio
        vel_y = 0
        
    cerchio_x = max(raggio, min(cerchio_x, LARGHEZZA - raggio))
    cerchio_y = max(raggio, min(cerchio_y, ALTEZZA - raggio))
    
    schermo.fill(NERO)
    pygame.draw.circle(schermo, BIANCO, (int(cerchio_x), int(cerchio_y)), raggio)
    
    pygame.display.update()
    
pygame.quit()
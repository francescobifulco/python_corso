"""7. Aggiungere un contatore di FPS
Visualizza sullo schermo gli FPS del programma 
aggiornati ogni frame, usando un oggetto `Clock()`."""

import pygame

pygame.init()

LARGHEZZA = 800
ALTEZZA = 600
TITOLO = 'Cambiare velocità tramite tastiera'

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
    
    fps = int(clock.get_fps())
    font = pygame.font.SysFont('Arial', 60, bold=True, italic=False)
    testo = font.render(f"FPS: {fps}", True , BIANCO)
    
    
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
    pygame.draw.circle(schermo, BIANCO, (cerchio_x, cerchio_y), raggio)
    schermo.blit(testo, (10, 10))
    
    pygame.display.update()
    
pygame.quit()
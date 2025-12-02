"""15. Applicare gravità a un oggetto
Simula la caduta libera: un rettangolo 
cade verso il basso con accelerazione 
costante. Impedisci che esca dallo 
schermo."""

import pygame

pygame.init()

LARGHEZZA = 800
ALTEZZA = 600
TITOLO = 'Applicare gravità a un oggetto'

NERO = (0, 0, 0)
BIANCO = (255, 255, 255)

clock = pygame.time.Clock()
FPS = 60 

schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption(TITOLO)

rettangolo = pygame.Rect(300, 50, 100, 50)

gravita = 0.5
velocita = 0

loop = True
while loop:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop = False
    
    
    velocita += gravita
    rettangolo.y += velocita 
    
    if rettangolo.bottom >= ALTEZZA:
        rettangolo.bottom = ALTEZZA
        velocita = 0
    
    schermo.fill(NERO)
    pygame.draw.rect(schermo, BIANCO, rettangolo, 0) 
       
    #rettangolo.clamp_ip(schermo.get_rect())
    pygame.display.update()
    
pygame.quit()
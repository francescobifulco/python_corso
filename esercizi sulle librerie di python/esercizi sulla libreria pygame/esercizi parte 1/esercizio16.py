"""16. Salto semplice con gravità
Aggiungi la possibilità di far 
saltare l’oggetto con la barra 
spaziatrice. Impedisci salti 
multipli mentre è in aria."""

import pygame

pygame.init()

LARGHEZZA = 800
ALTEZZA = 600
TITOLO = 'Salto semplice con gravità'

NERO = (0, 0, 0)
BIANCO = (255, 255, 255)

clock = pygame.time.Clock()
FPS = 60 

schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption(TITOLO)

rettangolo = pygame.Rect(300, 50, 100, 50)

gravita = 0.5
velocita = 0
forza_salto = -12   
a_terra = False

loop = True
while loop:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and a_terra:
                velocita = forza_salto
                a_terra = False

    velocita += gravita
    rettangolo.y += velocita

    if rettangolo.bottom >= ALTEZZA:
        rettangolo.bottom = ALTEZZA
        velocita = 0
        a_terra = True   
    
    
    schermo.fill(NERO)
    pygame.draw.rect(schermo, BIANCO, rettangolo)
    pygame.display.update()

pygame.quit()

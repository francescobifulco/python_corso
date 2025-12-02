
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

# Giocatore
giocatore = pygame.Rect(300, 50, 100, 50)

gravita = 0.5
velocita_y = 0
forza_salto = -12
a_terra = False

loop = True
while loop:
    clock.tick(FPS)

    # --- Gestione eventi ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop = False

        if evento.type == pygame.KEYDOWN:
            # Salto
            if evento.key == pygame.K_SPACE and a_terra:
                velocita_y = forza_salto
                a_terra = False

    # --- Fisica ---
    velocita_y += gravita
    giocatore.y += velocita_y

    # --- Collisione col terreno ---
    if giocatore.bottom >= ALTEZZA:
        giocatore.bottom = ALTEZZA
        velocita_y = 0
        a_terra = True

    # --- Disegno ---
    schermo.fill(NERO)
    pygame.draw.rect(schermo, BIANCO, giocatore)
    pygame.display.update()

pygame.quit()

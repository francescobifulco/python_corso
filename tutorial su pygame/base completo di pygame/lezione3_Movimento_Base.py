import pygame

pygame.init()

LARGHEZZA, ALTEZZA = 800, 600
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Movimento Base")

# Colori
BIANCO = (255, 255, 255)
ROSSO = (255, 0, 0)
NERO = (0, 0, 0)

# Clock e FPS
clock = pygame.time.Clock()
FPS = 60 # 60 frame al secondo

# Oggetto Giocatore
player_size = 50
player_x = LARGHEZZA // 2 - player_size // 2
player_y = ALTEZZA - player_size - 10
player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
player_vel = 5

running = True
while running:
    # Imposta la velocità massima del loop (FPS)
    clock.tick(FPS)

    # Gestione degli Eventi
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    # Input da tastiera (Controlli)
    # Restituisce un dizionario con lo stato di tutti i tasti premuti
    tasti_premuti = pygame.key.get_pressed()

    if tasti_premuti[pygame.K_LEFT]:
        player_rect.x -= player_vel
    if tasti_premuti[pygame.K_RIGHT]:
        player_rect.x += player_vel
    if tasti_premuti[pygame.K_UP]:
        player_rect.y -= player_vel
    if tasti_premuti[pygame.K_DOWN]:
        player_rect.y += player_vel
        
    # Limita il giocatore ai bordi dello schermo
    player_rect.clamp_ip(schermo.get_rect()) # clamping in place

    # Disegno / Rendering
    schermo.fill(NERO)
    pygame.draw.rect(schermo, ROSSO, player_rect)

    pygame.display.flip()

pygame.quit()
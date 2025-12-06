import pygame
pygame.init()

# -----------------------
# Impostazioni base
# -----------------------
LARGHEZZA = 800
ALTEZZA = 600
SCHERMO = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
clock = pygame.time.Clock()

# Colori
BIANCO = (255, 255, 255)
NERO = (0, 0, 0)
ROSSO = (255, 0, 0)
VERDE = (0, 255, 0)

# -----------------------
# GRAVITÀ e FISICA
# -----------------------
GRAVITA = 0.5
VELOCITA_SALTO = -10
VELOCITA_MOV = 5


# -----------------------
# Classe Giocatore
# -----------------------
class Giocatore:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 60)
        self.vel_y = 0
        self.on_ground = False

    def movimento(self):
        tasti = pygame.key.get_pressed()

        # Movimento orizzontale
        if tasti[pygame.K_a]:
            self.rect.x -= VELOCITA_MOV
        if tasti[pygame.K_d]:
            self.rect.x += VELOCITA_MOV

        # Salto
        if tasti[pygame.K_SPACE] and self.on_ground:
            self.vel_y = VELOCITA_SALTO
            self.on_ground = False

    def applica_gravità(self, piattaforme):
        self.vel_y += GRAVITA
        self.rect.y += self.vel_y

        # Controllo collisioni
        self.on_ground = False
        for piattaforma in piattaforme:
            if self.rect.colliderect(piattaforma):

                # Il giocatore sta cadendo
                if self.vel_y > 0:
                    self.rect.bottom = piattaforma.top
                    self.vel_y = 0
                    self.on_ground = True

    def disegna(self, superficie):
        pygame.draw.rect(superficie, ROSSO, self.rect)


# -----------------------
# Piattaforme
# -----------------------
piattaforme = [
    pygame.Rect(0, 550, 800, 50),       # pavimento
    pygame.Rect(200, 400, 200, 20),
    pygame.Rect(500, 300, 200, 20),
    pygame.Rect(100, 200, 150, 20)
]

giocatore = Giocatore(100, 100)

# -----------------------
# Loop principale del gioco
# -----------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    giocatore.movimento()
    giocatore.applica_gravità(piattaforme)

    # -----------------------
    # Disegno
    # -----------------------
    SCHERMO.fill(BIANCO)

    # Piattaforme
    for piattaforma in piattaforme:
        pygame.draw.rect(SCHERMO, VERDE, piattaforma)

    # Giocatore
    giocatore.disegna(SCHERMO)

    pygame.display.update()
    clock.tick(60)

pygame.quit()

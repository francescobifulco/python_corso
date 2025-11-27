import pygame
import random

pygame.init()
LARGHEZZA, ALTEZZA = 800, 600
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Collisione tra Giocatore e Nemici")

# Colori
BIANCO = (255, 255, 255)
NERO = (0, 0, 0)

# Clock e FPS
clock = pygame.time.Clock()
FPS = 60 # 60 frame al secondo

# -- Classe Giocatore --
class Giocatore(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Chiama il costruttore della classe base (Sprite)
        super().__init__() 
        
        self.image = pygame.Surface([50, 50]) # Crea una superficie 50x50
        self.image.fill(BIANCO) # Colore del giocatore
        self.rect = self.image.get_rect() # Ottiene il Rect dalla superficie
        self.rect.x = x
        self.rect.y = y
        self.vel = 5

    def update(self):
        # Logica di aggiornamento (es. movimento automatico)
        # In questo esempio, gestiamo il movimento nell'Event Loop

        # Gestione dell'input (movimento)
        tasti_premuti = pygame.key.get_pressed()
        if tasti_premuti[pygame.K_LEFT]:
            self.rect.x -= self.vel
        if tasti_premuti[pygame.K_RIGHT]:
            self.rect.x += self.vel
        if tasti_premuti[pygame.K_UP]:
            self.rect.y -= self.vel
        if tasti_premuti[pygame.K_DOWN]:
            self.rect.y += self.vel

        # Mantiene il giocatore sullo schermo
        self.rect.clamp_ip(schermo.get_rect())

# -- Classe Nemico --
class Nemico(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill((0, 255, 0)) # Verde
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 3

    def update(self):
        self.rect.y += self.vel_y
        # Se il nemico è fuori dallo schermo, si riposiziona
        if self.rect.top > ALTEZZA:
            self.rect.x = random.randrange(LARGHEZZA - 30)
            self.rect.y = random.randrange(-100, -50)

# Creazione dei gruppi
giocatore = Giocatore(LARGHEZZA // 2, ALTEZZA - 60)
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

all_sprites.add(giocatore)

# Generazione di nemici casuali
for i in range(8):
    x = random.randrange(LARGHEZZA - 30)
    y = random.randrange(-100, -40)
    nemico = Nemico(x, y)
    all_sprites.add(nemico)
    enemies.add(nemico)


running = True
while running:
    clock.tick(FPS)

    # --- Eventi ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Update ---
    all_sprites.update()

    # --- Collisione ---
    # Rilevamento Collisioni
    # Controlla se il giocatore collide con uno qualsiasi dei nemici
    # True: elimina il nemico se colpito
    collisioni = pygame.sprite.spritecollide(giocatore, enemies, True)

    if collisioni:
        print("Gioco Finito! (Collisione rilevata)")
        running = False
        # logica di fine gioco...

    # --- Disegno ---
    schermo.fill(NERO)
    all_sprites.draw(schermo)
    pygame.display.flip()

pygame.quit()
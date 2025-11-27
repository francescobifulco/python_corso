import pygame

pygame.init()
LARGHEZZA, ALTEZZA = 800, 600
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Creazione di una Classe Giocatore (Sprite)")

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
        
# ... (setup di Pygame, colori, clock)

# Creazione degli oggetti Giocatore e Gruppi
giocatore = Giocatore(LARGHEZZA // 2, ALTEZZA - 60)

# Gruppo per tutti gli sprite
all_sprites = pygame.sprite.Group()
all_sprites.add(giocatore)

running = True
while running:
    clock.tick(FPS)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
            
    # Aggiornamento
    # Chiama il metodo update() di tutti gli sprite nel gruppo
    all_sprites.update() 
    
    # Disegno / Rendering
    schermo.fill(NERO)
    # Disegna tutti gli sprite nel gruppo sullo schermo
    all_sprites.draw(schermo) 
    
    pygame.display.flip()

pygame.quit()